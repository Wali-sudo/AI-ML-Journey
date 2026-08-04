#datatypes
#dtypes() is a function that returns the data types of the columns in a DataFrame. It is used to check the data types of each column in a DataFrame, which can be useful for data analysis and manipulation.
#astypes() is a function that converts the data types of the columns in a DataFrame. It is used to change the data types of each column in a DataFrame, which can be useful for data analysis and manipulation.

reviews.price.dtype

reviews.points.astype('float64')



#missing values

#Entries missing values are given the value NaN, short for "Not a Number". For technical reasons these NaN values are always of the float64 dtype.
#Pandas provides some methods specific to missing data. To select NaN entries you can use pd.isnull() 

reviews[pd.isnull(reviews.country)]

#.fillna(): Replaces missing values with a specific value.
# Replace NaN in the 'country' column with 'Unknown'
reviews.country = reviews.country.fillna('Unknown')

#dropna(): Removes missing values from a DataFrame. By default, it removes any row that contains at least one NaN value. You can also specify a subset of columns to check for NaN values.
# Drop all rows that have any missing values
reviews_clean = reviews.dropna()

# Drop rows where 'price' specifically is missing
reviews_clean = reviews.dropna(subset=['price'])