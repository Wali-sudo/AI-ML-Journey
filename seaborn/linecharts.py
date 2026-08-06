import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
spotify_data=pd.read_csv('/home/waliahmad/Downloads/spotify.csv', index_col=0)
print(spotify_data.head())
print(spotify_data.tail())

# Line chart showing daily global streams of each song 
#sns.lineplot(data=spotify_data)

#setting the width and height of the figure
plt.figure(figsize=(14, 7))

#setting the title of the figure
plt.title('Daily Global Streams of Each Song', fontsize=16)

# setting the x-axis label
plt.xlabel('Date', fontsize=14)

# setting the y-axis label
plt.ylabel('Global Streams', fontsize=14)

#sns.lineplot(data=spotify_data)

#plot a subset of the data for better visualization
sns.lineplot(data=spotify_data['Shape of You'], label='Shape of You')#label is used to give a name to the line in the graph
sns.lineplot(data=spotify_data['Despacito'], label='Despacito')
plt.show()