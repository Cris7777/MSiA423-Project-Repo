import pandas as pd

def test_loaddata():
    data = pd.read_csv('data/data1.csv', header=0)
    row = data.shape[0]
    col = data.shape[1]

    row_true = 17907
    col_true = 51

    assert row == row_true
    assert col == col_true
