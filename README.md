# Startup Funding Analysis

## Overview

This project is a web application for analyzing startup funding data using Streamlit. It allows users to explore funding details, analyze investors, and review startup-specific insights. The app processes and visualizes a dataset of startup funding information.

## Features

1. **Overall Analysis**: Provides an overview of the funding landscape.
2. **Startup Analysis**: Offers detailed insights into individual startups.
3. **Investor Analysis**: Focuses on individual investors and their investments.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Dataset

The application uses a CSV file (`startup_funding.csv`) located at:
`/Users/shiv_sharan/Desktop/datasets/startup_funding.csv`

### Dataset Preparation
- The `Remarks` column is removed.
- Columns are renamed for clarity:
  - `Date dd/mm/yyyy` -> `Date`
  - `Startup Name` -> `Startup`
  - `Industry Vertical` -> `Vertical`
  - `SubVertical` -> `subvertical`
  - `City  Location` -> `City`
  - `Investors Name` -> `Investors`
  - `InvestmentnType` -> `round`
  - `Amount in USD` -> `Amount`
- Missing values are handled:
  - `Investors` column filled with `undisclosed`.
  - `Amount` column filled with `0`.
- Amount values are cleaned and converted to Indian Rupees (INR).
- Date column is standardized.

## Application Structure

### Sidebar Options
- **Overall Analysis**: Displays aggregated metrics and trends.
- **Startup**: Allows selecting a startup for detailed analysis.
- **Investor**: Enables exploring investment details for a specific investor.

### Core Functions
- **`usd_to_inr`**: Converts USD to INR.
- **`clean_date_column`**: Standardizes the `Date` column.
- **`load_general_analysis`**: Displays overall funding insights.
- **`load_investors_details`**: Provides detailed information on selected investors.

## Usage

1. Launch the app using `streamlit run app.py`.
2. Select a feature from the sidebar:
   - For overall funding trends, choose `Overall Analysis`.
   - To analyze specific startups, select `Startup` and pick a startup.
   - To explore investor activity, select `Investor` and pick an investor.

## Requirements
- Python 3.7+
- Libraries:
  - Streamlit
  - Pandas
  - Custom functions (imported from `func`)

## File Structure
- `app.py`: Main application script.
- `func.py`: Contains utility functions (`usd_to_inr`, `clean_date_column`, etc.).
- `startup_funding.csv`: Dataset for analysis.

## Acknowledgements
This project uses a dataset of startup funding details to demonstrate data cleaning, analysis, and visualization techniques.

## Future Enhancements
- Add more visualization options.
- Include filters for funding rounds and industries.
- Enhance performance for larger datasets.

