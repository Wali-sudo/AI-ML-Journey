#renaming
#rename() is used to rename the index or columns of a DataFrame. It can take a dictionary or a function as an argument to specify the new names.

reviews.rename(columns={'points': 'score'})#changes the column name 'points' to 'score'

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})#changes the index 0 to 'firstEntry' and index 1 to 'secondEntry',dictionary is used to specify the new names for the index.

reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')



#concat() Glues DataFrames together along an axis (either row-wise or column-wise). Useful when datasets have the same columns or indexes.
combined_df = pd.concat([canadian_wines, australian_wines])
#merge() Joins DataFrames based on matching values in specific columns (similar to SQL JOIN).
merged_df = pd.merge(wines, prices, on='wine_id', how='inner')# do have inner, outer, left, right joins