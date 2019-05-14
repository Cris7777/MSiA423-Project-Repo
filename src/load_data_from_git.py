import pandas as pd

url = 'https://raw.githubusercontent.com/Cris7777/MSiA423_data/master/data1.csv'
df = pd.read_csv(url, index_col=0)
df.to_csv('../data/data1.csv')
