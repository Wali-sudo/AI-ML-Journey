#inedxing
import pandas as pd 
spotify_data=pd.read_csv('/home/waliahmad/Downloads/most_streamed_spotify_2025.csv',index_col=0)
print(spotify_data.head())
#1
print(spotify_data.track)
#2
print(spotify_data['track'])
print(spotify_data[['track', 'artist', 'billed_artist_count']])
#3
#index based selections
#iloc syntax:
#iloc[0] means 1st row and all columns 
#iloc[0,0] means 1st row and 1st column
#iloc[0:5] first 5 rows and all columns
#iloc[0:5,0:5] first 5 rows and first 5 columns
#iloc[:,0:5] all rows and first 5 columns
# Select rows 0, 2, and 4
#iloc[[0, 2, 4]]
# Select rows 0 and 2, and columns 1 and 3
#iloc[[0, 2], [1, 3]]
#for bottom access we can use neg numbers
print(spotify_data.iloc[0,0:3])

#label based selections
#iloc works with index numbering for both rows and columns and loc works with the column names and the index label
print(spotify_data.loc[1,['track', 'artist', 'billed_artist_count']])

#Manipulating the index in Pandas simply means changing, modifying, or resetting how your rows are identified

#At the moment of loading data: You can use index_col inside pd.read_csv() to choose a specific column from your file to act as the index right away.
#After loading into memory: You can manipulate that DataFrame's index at any point using .set_index() to set a new column as row labels, or .reset_index() to revert back to default row numbers (0, 1, 2...).
spotify_data=pd.read_csv('/home/waliahmad/Downloads/most_streamed_spotify_2025.csv')
spotify_data=spotify_data.set_index('rank')
print(spotify_data)

#Conditional selection (also called boolean indexing or filtering) is how you extract specific rows from a DataFrame based on conditions—like "Show me all songs with over 1 billion streams" or "Show me tracks by Lady Gaga."
is_Alex=spotify_data['artist']=='Alex Warren'
alex_tracks=spotify_data[is_Alex]
print(alex_tracks)

alex_tracks=spotify_data.loc[spotify_data['artist']=='Alex Warren']
print(alex_tracks)

#use notnull() for checking if the index is empty
#we can also add multiple conditions

#Assiging Data
# Creates a new column named 'platform' and fills every row with 'Spotify'
spotify_data['platform'] = 'Spotify'
print(spotify_data)
spotify_data['streams_in_lac']=spotify_data['daily_streams']/100000;
print(spotify_data)