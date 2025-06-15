import pandas as pd

def enrich(df_trans, df_cust, df_prod):
    df = df_trans.merge(df_cust, on='customer_id')
    df = df.merge(df_prod, on='product_id')
    return df
