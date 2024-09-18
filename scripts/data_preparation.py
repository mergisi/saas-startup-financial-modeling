# data_preparation.py
"""
Script to clean and prepare raw SaaS data for analysis.
"""

import pandas as pd
import argparse

def prepare_data(input_file, output_file):
    # Read the raw data
    df = pd.read_csv(input_file)
    
    # Data cleaning steps
    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort by date
    df.sort_values('Date', inplace=True)
    
    # Reset index
    df.reset_index(drop=True, inplace=True)
    
    # Save the cleaned data
    df.to_csv(output_file, index=False)
    print(f"Data prepared and saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Prepare SaaS data for analysis.')
    parser.add_argument('--input', type=str, default='../data/raw_saas_data.csv', help='Input CSV file')
    parser.add_argument('--output', type=str, default='../data/saas_metrics.csv', help='Output CSV file')
