import pandas as pd

def clean_transactions(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df[df['amount'] > 0]  # Remove invalid/negative transactions
    return df
