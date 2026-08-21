import pandas as pd 
melbourne_data = pd.read_csv('/home/waliahmad/Downloads/melb_data.csv')
print(melbourne_data.describe())# describe is used for statistical summary of the data
print(melbourne_data.head())
print(melbourne_data.tail())

