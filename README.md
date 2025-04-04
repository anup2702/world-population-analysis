# World Population Analysis

A web application for analyzing and visualizing global population data. This application provides interactive visualizations and insights into world population trends, density, and growth rates.

## Features

- **Population Distribution Analysis**: View top and bottom populated countries
- **Population Density Analysis**: Analyze population density across countries
- **Growth Rate Analysis**: Explore population growth trends
- **Interactive World Maps**: Visualize population distribution and growth rates on a world map
- **Summary Statistics**: Get comprehensive statistical insights about global population

## Technologies Used

- **Backend**: Python, Flask
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Frontend**: HTML, CSS, Bootstrap 5, Font Awesome
- **Data Source**: World Population Excel file

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/anup2702/world-population-analysis.git
   cd world-population-analysis
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Project Structure

```
world-population-analysis/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── world_population.xlsx   # Data source
├── templates/              # HTML templates
│   ├── index.html          # Home page
│   └── results.html        # Results page
├── generate_static_site.py # Script to generate static site for GitHub Pages
└── README.md               # Project documentation
```

## Usage

1. The application automatically loads the world population data from the Excel file
2. Navigate through the different tabs to explore various analyses:
   - Population Distribution
   - Population Density
   - Growth Rate
   - Interactive Maps
   - Summary Statistics

## Deployment

### Local Deployment

Run the Flask application locally:
```
python app.py
```

### GitHub Pages Deployment

This project can be deployed to GitHub Pages as a static site:

1. Push your code to GitHub
2. The GitHub Actions workflow will automatically generate the static site and deploy it to GitHub Pages
3. Your site will be available at: `https://anup2702.github.io/world-population-analysis/`

To manually generate the static site:
```
python generate_static_site.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data sourced from publicly available world population statistics
- Inspired by the need for better visualization of global demographic trends 