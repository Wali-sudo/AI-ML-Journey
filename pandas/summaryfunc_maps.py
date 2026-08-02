#Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way
#.describe(): Generates high-level summary statistics (count, mean, std, min, max, percentiles for numerical columns; unique, top, freq for categorical columns)
import pandas as pd
spotify_data=pd.read_csv('/home/waliahmad/Downloads/most_streamed_spotify_2025.csv')
print(spotify_data.describe())
print(spotify_data['daily_streams'].describe())
#.mean(), .median(), .std(): Calculates specific statistical metrics.
#.unique(): Extracts a list of all unique values in a column.
print(spotify_data['artist'].unique())
#.value_counts(): Counts the occurrences of each unique value in a column.
print(spotify_data['artist'].value_counts())#counted the number of times each artist appears in the dataset



#maps

#Imagine you have a huge line of raw apples, and you want to turn every single one into a glass of apple juice.
#You line up your data (your column of apples), set the machine's instruction ("squeeze into juice"), and the machine runs down the line, performing that exact step on every single item, one by one.

#Instead of changing numbers or words in your dataset manually one by one (which would take forever!), a map does it automatically to the entire column.

#1. Series.map(): Applies a function to each element in a pandas Series.
#simple math function(lambda function)
spotify_data['daily_streams'] = spotify_data['daily_streams'].map(lambda x: x * 2)#doubles the daily streams for each song in the dataset
#dictionary mapping
mapping_dict = {'Ed Sheeran': 'Pop', 'Taylor Swift': 'Pop', 'Drake': 'Hip-Hop', 'Adele': 'Pop', 'BTS': 'K-Pop'}
spotify_data['genre'] = spotify_data['artist'].map(mapping_dict)#maps the artist names to their corresponding genres using the mapping_dict
#custom function mapping
def categorize_streams(streams):
    if streams < 1000000:
        return 'Low'
    elif streams < 5000000:
        return 'Medium'
    else:
        return 'High'
spotify_data['stream_category'] = spotify_data['daily_streams'].map(categorize_streams)#categorizes the daily streams into 'Low', 'Medium', or 'High' based on the number of streams using the categorize_streams function
#2. DataFrame.map(): Applies a function to each element in a pandas DataFrame.
#apply(): Applies a function along an axis of the DataFrame (rows or columns).
spotify_data = spotify_data.apply(lambda x: x * 2,axis=0)#doubles the daily streams for each song in the dataset using apply() instead of map() in this case, axis=0 indicates that the function is applied to each column (which is the default behavior for apply() on a Series).
#if we select a single column from the DataFrame, it returns a Series, and we can use map() on that Series. If we select multiple columns, it returns a DataFrame, and we can use apply() on that DataFrame.
#also we can not use axis when select a single column, because it is a Series, not a DataFrame. The axis parameter is only relevant when working with DataFrames, where you can specify whether to apply the function along rows (axis=0) or columns (axis=1).