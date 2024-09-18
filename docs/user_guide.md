# User Guide

## Introduction

This guide provides instructions on how to use the notebooks and scripts included in this repository.

## Notebooks

### Opening a Notebook

1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Navigate to the Notebook**:
   - Go to the `notebooks/` directory.
   - Click on the notebook you wish to open:
     - `revenue_forecasting.ipynb`
     - `churn_analysis.ipynb`
     - `cohort_analysis.ipynb`
     - `unit_economics.ipynb`

### Running the Notebook

- **Sequential Execution**: Run the cells in order by clicking Cell > Run All.
- **Interactive Execution**: Run cells individually using Shift + Enter.

## Scripts

### Running a Script

1. **Navigate to the `scripts/` Directory**:
   ```bash
   cd scripts/
   ```

2. **Execute the Script**:
   - Data Preparation:
     ```bash
     python data_preparation.py --input ../data/raw_saas_data.csv --output ../data/saas_metrics.csv
     ```
   - KPI Calculations:
     ```bash
     python kpi_calculations.py --datafile ../data/saas_metrics.csv
     ```

### Script Parameters

Use the `--help` flag to see available options:
```bash
python data_preparation.py --help
```

## Data

- **Accessing Data**: Data files are located in the `data/` directory.
- **Custom Data**: You can replace the sample data with your own datasets.
  - Ensure that the data format matches the expected structure.

## Tips

- **Virtual Environment**: Use a virtual environment to manage dependencies.
- **Backup**: Keep a backup of your data and any changes you make to the notebooks.

For questions or issues, please open an issue on the GitHub repository.
