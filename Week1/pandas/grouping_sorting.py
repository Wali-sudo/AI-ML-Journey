#grouping
#Grouping allows you to split a DataFrame into groups based on values in one or more columns, apply a function (like calculation or aggregation) to each group, and combine the results into a new Data Structure.
#syntax: df.groupby('column_name')['target_column'].aggregation_function()
reviews.groupby('points').points.count()

#You can think of each group we generate as being a slice of our DataFrame containing only data with values that match. This DataFrame is accessible to us directly using the apply() method, and we can then manipulate the data in any way we see fit.
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

#When you use .groupby() with two or more columns, Pandas automatically creates a MultiIndex on the resulting Series or DataFrame to represent the nested structure of your groups.
#For even more fine-grained control, you can also group by more than one column. For an example, here's how we would pick out the best wine by country and province:
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])#idxmax() returns the index of the maximum value in a Series. In this case, we are using it to find the index of the row with the highest points for each group of country and province

#Another groupby() method worth mentioning is agg(), which lets you run a bunch of different functions on your DataFrame simultaneously
reviews.groupby(['country']).price.agg([len, min, max])
#if agg(consist of one function then it returns a Series, if consist of multiple functions then it returns a DataFrame with each function as a column.)

#sorting 
#Sorting reorganizes the order of rows or columns based on their values or their index labels.
# Sort rows by 'price' in ascending order (default)
df.sort_values(by='price')
# Sort rows by 'price' in descending order
df.sort_values(by='price', ascending=False)
# Sort by multiple columns (e.g., 'country' A-Z, then 'points' high-to-low)
df.sort_values(by=['country', 'points'], ascending=[True, False])

#Used to reorder rows or columns based on their row labels/indexes rather than their column values.
# Sort rows by index labels numerically or alphabetically
df.sort_index()
# Sort in descending order
df.sort_index(ascending=False)