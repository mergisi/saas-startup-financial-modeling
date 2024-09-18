# kpi_calculations.py
"""
Script to calculate key SaaS KPIs like MRR, ARR, and churn rate.
"""

import pandas as pd
import argparse

def calculate_kpis(data_file):
    df = pd.read_csv(data_file, parse_dates=['Date'])
    
    # Calculate MRR (Monthly Recurring Revenue)
    df['MRR'] = df['Revenue']
    
    # Calculate ARR (Annual Recurring Revenue)
    df['ARR'] = df['MRR'] * 12
    
    # Calculate Churn Rate
    df['Churn_Rate'] = df['Churned_Customers'] / df['Total_Customers'].shift(1)
    df['Churn_Rate'].fillna(0, inplace=True)
    
    # Calculate Customer Acquisition Cost (CAC)
    if 'Marketing_Expenses' in df.columns:
        df['CAC'] = df['Marketing_Expenses'] / df['New_Customers']
    else:
        df['CAC'] = None  # Placeholder if marketing expenses are not available
    
    # Save the KPIs to a new CSV file
    kpi_columns = ['Date', 'MRR', 'ARR', 'Churn_Rate', 'CAC']
    df[kpi_columns].to_csv('../data/saas_kpis.csv', index=False)
    print("KPIs calculated and saved to ../data/saas_kpis.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate SaaS KPIs.')
    parser.add_argument('--datafile', type=str, default='../data/saas_metrics.csv', help='Input CSV file with SaaS metrics')
    
    args = parser.parse_args()
    calculate_kpis(args.datafile)
