import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

# Import the WorldPopulationAnalysis class from app.py
from app import WorldPopulationAnalysis

def generate_static_site():
    # Create output directories
    os.makedirs('docs', exist_ok=True)
    os.makedirs('docs/images', exist_ok=True)
    os.makedirs('docs/css', exist_ok=True)
    os.makedirs('docs/js', exist_ok=True)
    
    # Copy CSS and JS files
    with open('templates/index.html', 'r') as f:
        index_html = f.read()
    
    # Extract CSS from the index.html
    css_start = index_html.find('<style>') + 7
    css_end = index_html.find('</style>')
    css_content = index_html[css_start:css_end]
    
    with open('docs/css/styles.css', 'w') as f:
        f.write(css_content)
    
    # Extract JS from the index.html
    js_start = index_html.find('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>')
    js_content = index_html[js_start:js_start + 100]
    
    with open('docs/js/scripts.js', 'w') as f:
        f.write(js_content)
    
    # Run the analysis
    analyzer = WorldPopulationAnalysis('world_population.xlsx')
    if analyzer.df is None:
        print("Error loading data. Please check the file format and make sure it contains the required columns.")
        return
    
    results = analyzer.run_analysis()
    
    # Save images to files
    with open('docs/images/top_10.png', 'wb') as f:
        f.write(base64.b64decode(results['top_10_img']))
    
    with open('docs/images/bottom_10.png', 'wb') as f:
        f.write(base64.b64decode(results['bottom_10_img']))
    
    with open('docs/images/density.png', 'wb') as f:
        f.write(base64.b64decode(results['density_img']))
    
    with open('docs/images/growth.png', 'wb') as f:
        f.write(base64.b64decode(results['growth_img']))
    
    # Save the maps as HTML files
    with open('docs/maps/population_map.html', 'w', encoding='utf-8') as f:
        f.write(results['pop_map'])
    
    with open('docs/maps/growth_map.html', 'w', encoding='utf-8') as f:
        f.write(results['growth_map'])
    
    # Generate the index.html file
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>World Population Analysis</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="card-header text-center">
                <h1><i class="fas fa-globe-americas me-2"></i>World Population Analysis</h1>
                <p class="mb-0">Comprehensive analysis of global population data</p>
            </div>
            <div class="card-body">
                <ul class="nav nav-tabs" id="analysisTabs" role="tablist">
                    <li class="nav-item">
                        <a class="nav-link active" id="distribution-tab" data-bs-toggle="tab" href="#distribution" role="tab">
                            <i class="fas fa-chart-bar me-2"></i>Population Distribution
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" id="density-tab" data-bs-toggle="tab" href="#density" role="tab">
                            <i class="fas fa-users me-2"></i>Population Density
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" id="growth-tab" data-bs-toggle="tab" href="#growth" role="tab">
                            <i class="fas fa-chart-line me-2"></i>Growth Rate
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" id="maps-tab" data-bs-toggle="tab" href="#maps" role="tab">
                            <i class="fas fa-map me-2"></i>Interactive Maps
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" id="summary-tab" data-bs-toggle="tab" href="#summary" role="tab">
                            <i class="fas fa-table me-2"></i>Summary Statistics
                        </a>
                    </li>
                </ul>
                
                <div class="tab-content" id="analysisTabContent">
                    <div class="tab-pane fade show active" id="distribution" role="tabpanel">
                        <div class="row">
                            <div class="col-md-6">
                                <div class="visualization-container">
                                    <h3 class="visualization-title">Top 10 Most Populated Countries</h3>
                                    <img src="images/top_10.png" class="img-fluid" alt="Top 10 Countries">
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="visualization-container">
                                    <h3 class="visualization-title">10 Least Populated Countries</h3>
                                    <img src="images/bottom_10.png" class="img-fluid" alt="Bottom 10 Countries">
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="tab-pane fade" id="density" role="tabpanel">
                        <div class="visualization-container">
                            <h3 class="visualization-title">Top 10 Countries by Population Density</h3>
                            <img src="images/density.png" class="img-fluid" alt="Population Density">
                        </div>
                    </div>
                    
                    <div class="tab-pane fade" id="growth" role="tabpanel">
                        <div class="visualization-container">
                            <h3 class="visualization-title">Top 10 Countries by Population Growth Rate</h3>
                            <img src="images/growth.png" class="img-fluid" alt="Growth Rate">
                        </div>
                    </div>
                    
                    <div class="tab-pane fade" id="maps" role="tabpanel">
                        <div class="visualization-container">
                            <h3 class="visualization-title">World Population Distribution</h3>
                            <div class="map-container">
                                <iframe src="maps/population_map.html" width="100%" height="500px" frameborder="0"></iframe>
                            </div>
                        </div>
                        <div class="visualization-container">
                            <h3 class="visualization-title">World Population Growth Rate</h3>
                            <div class="map-container">
                                <iframe src="maps/growth_map.html" width="100%" height="500px" frameborder="0"></iframe>
                            </div>
                        </div>
                    </div>
                    
                    <div class="tab-pane fade" id="summary" role="tabpanel">
                        <div class="visualization-container">
                            <h3 class="visualization-title">Summary Statistics</h3>
                            <div class="table-responsive">
                                ''' + results['summary_html'] + '''
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/scripts.js"></script>
</body>
</html>''')
    
    print("Static site generated successfully in the 'docs' directory.")
    print("You can now push this to GitHub Pages by setting the 'docs' directory as the source in your repository settings.")

if __name__ == "__main__":
    generate_static_site() 