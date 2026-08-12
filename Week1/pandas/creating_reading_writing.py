#Kaggle
import pandas as pd
#creating data: There are two core objects in pandas: the DataFrame and the Series.
#data frame: A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.
#A DataFrame is an entire table made of multiple columns (2-Dimensional).
fpd=pd.DataFrame({'Yes':[45,46],'No':[23,43]})
print(fpd)
#Raw datasets in the real world are notorious for being messy—full of missing values, typos, inconsistent formats, unlabelled columns, and irrelevant data.
#A DataFrame acts as your cleaning, organizing, and structuring tool to turn that raw chaos into a neat, production-ready table.
fpd=pd.DataFrame({'Wali':['I liked it','It was awful'],'Amna':['Pretty Good','Bland']},index=['Product A','Product B'])
print(fpd)
#A Series is a single column (1-Dimensional).
spd=pd.Series([23,56,78])
print(spd)
spd=pd.Series({'Wali':[45,56,23]})
print(spd)
spd=pd.Series([34,56,21],index=['Wali','Noor','Amna'])
print(spd)
#if you want to name the column like we had done in the dataframes then we need to pass a separate list known as name
spd=pd.Series([34,56,21],index=['Wali','Noor','Amna'],name='Marks')
print(spd)


#reading data
spotify_data=pd.read_csv('/home/waliahmad/Downloads/most_streamed_spotify_2025.csv')
print(spotify_data.head())#Inspect the first 5 rows to confirm it loaded properly
print(spotify_data.shape)#shape attribute to check how large the resulting DataFrame is

#for specific columns
#df = pd.read_csv('data.csv', usecols=['Name', 'Age', 'Salary'])

#Tell Pandas what values should be treated as empty
#df = pd.read_csv('data.csv', na_values=['N/A', 'Unknown', '-'])

#if csv file has an built in index column,pandas doesnt pick it up automatically,If your CSV already includes an index column (like IDs or row numbers as column 0) use indexcol
spotify_data=pd.read_csv('/home/waliahmad/Downloads/most_streamed_spotify_2025.csv',index_col=0)
print(spotify_data.head())


#writing data
# 1. Create a sample DataFrame
df = pd.DataFrame({
    'Apples': [30, 21],
    'Bananas': [35, 41]
}, index=['2017 Sales', '2018 Sales'])
# 2. Export to CSV file
df.to_csv('fruit_sales.csv')
#If your rows do not have meaningful index names and just use numbers (0, 1, 2), pass index=False
df.to_csv('fruit_sales.csv', index=False)

# Create a sample Series
fruit_series = pd.Series([30, 35], index=['Apples', 'Bananas'], name='Quantity')

# Export to CSV
fruit_series.to_csv('fruit_quantities.csv')