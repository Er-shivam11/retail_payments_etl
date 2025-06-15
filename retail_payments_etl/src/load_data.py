import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = load_csv('data/transactions.csv')  # fixed relative path
    print(df.head())
