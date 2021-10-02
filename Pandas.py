## Loading data into Pandas

import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df)

## Read Headers
# print(df.columns)

## Read each Column
print(df['Name'])
