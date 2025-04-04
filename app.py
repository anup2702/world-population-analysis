from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import base64
from io import BytesIO
import matplotlib
import sys

# Ensure the templates directory is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

matplotlib.use('Agg')  # Use non-interactive backend

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
app.secret_key = 'world_population_analysis_secret_key'

class WorldPopulationAnalysis:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.load_data()
        
    def load_data(self):
        try:
            if not os.path.exists(self.data_path):
                print(f"File not found: {self.data_path}")
                return False
                
            self.df = pd.read_excel(self.data_path)
            print(f"Successfully loaded data from {self.data_path}")
            print(f"Columns found: {list(self.df.columns)}")
            
            # Rename columns to match expected format
            column_mapping = {
                'Country/Territory': 'Country',
                '2022 Population': 'Population',
                'Density (per km²)': 'Density',
                'Growth Rate': 'Growth Rate'
            }
            
            # Check if all required columns exist
            missing_columns = [col for col in column_mapping.keys() if col not in self.df.columns]
            if missing_columns:
                print(f"Missing columns: {missing_columns}")
                return False
                
            # Rename columns
            self.df = self.df.rename(columns=column_mapping)
            
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
            
    def create_visualization(self, data, x_col, y_col, title):
        plt.figure(figsize=(12, 6))
        sns.barplot(data=data, x=x_col, y=y_col)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
        plt.close()
        
        return img_base64
            
    def analyze_population_distribution(self):
        top_10 = self.df.nlargest(10, 'Population')
        bottom_10 = self.df.nsmallest(10, 'Population')
        
        top_10_img = self.create_visualization(top_10, 'Country', 'Population', 'Top 10 Most Populated Countries')
        bottom_10_img = self.create_visualization(bottom_10, 'Country', 'Population', '10 Least Populated Countries')
        
        return top_10_img, bottom_10_img
        
    def analyze_population_density(self):
        top_10_density = self.df.nlargest(10, 'Density')
        return self.create_visualization(top_10_density, 'Country', 'Density', 'Top 10 Countries by Population Density')
        
    def analyze_growth_rate(self):
        top_10_growth = self.df.nlargest(10, 'Growth Rate')
        return self.create_visualization(top_10_growth, 'Country', 'Growth Rate', 'Top 10 Countries by Population Growth Rate')
        
    def create_interactive_visualization(self):
        fig_pop = px.choropleth(self.df,
                           locations='Country',
                           locationmode='country names',
                           color='Population',
                           title='World Population Distribution',
                           color_continuous_scale='Viridis')
        pop_map = fig_pop.to_html(full_html=False)
        
        fig_growth = px.choropleth(self.df,
                           locations='Country',
                           locationmode='country names',
                           color='Growth Rate',
                           title='World Population Growth Rate',
                           color_continuous_scale='RdBu')
        growth_map = fig_growth.to_html(full_html=False)
        
        return pop_map, growth_map
        
    def generate_summary_statistics(self):
        return self.df.describe().to_html()
        
    def run_analysis(self):
        top_10_img, bottom_10_img = self.analyze_population_distribution()
        density_img = self.analyze_population_density()
        growth_img = self.analyze_growth_rate()
        pop_map, growth_map = self.create_interactive_visualization()
        summary_html = self.generate_summary_statistics()
        
        return {
            'top_10_img': top_10_img,
            'bottom_10_img': bottom_10_img,
            'density_img': density_img,
            'growth_img': growth_img,
            'pop_map': pop_map,
            'growth_map': growth_map,
            'summary_html': summary_html
        }

@app.route('/')
def index():
    # Check if the file exists
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'world_population.xlsx')
    if not os.path.exists(file_path):
        flash(f'Error: The file {file_path} was not found. Please make sure it exists in the project directory.')
        return render_template('index.html')
    
    # Run analysis directly with the existing file
    analyzer = WorldPopulationAnalysis(file_path)
    if analyzer.df is None:
        flash('Error loading data. Please check the file format and make sure it contains the required columns.')
        return render_template('index.html')
    
    results = analyzer.run_analysis()
    return render_template('results.html', results=results)

if __name__ == '__main__':
    # Use production settings when deployed, development settings locally
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 