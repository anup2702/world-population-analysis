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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data sourced from publicly available world population statistics
- Inspired by the need for better visualization of global demographic trends 