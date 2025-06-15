def test_amount_positive():
    import pandas as pd
    df = pd.read_csv('../data/transactions.csv')
    assert (df['amount'] >= 0).all(), "Negative amount exists!"
