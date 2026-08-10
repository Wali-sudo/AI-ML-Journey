import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
flight_data=pd.read_csv('/home/waliahmad/Downloads/flight_delays.csv', index_col=0)
print(flight_data.head())
print(flight_data.tail())

plt.figure(figsize=(14, 7))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
#syntax for barplot is sns.barplot(data=dataframe, x=column_name, y=column_name)
sns.barplot(data=flight_data, x=flight_data.index, y='NK')#showing the average arrival delay for Spirit Airlines flights by month using a bar chart

plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Arrival Delay (minutes)', fontsize=14)
#plt.show()

plt.figure(figsize=(14, 7))
plt.title("Average Arrival Delay for Each Airline, by Month")
#syntax for heatmap is sns.heatmap(data=dataframe, annot=True, fmt='d', cmap='YlGnBu'),annot is used to show the values in the heatmap, fmt is used to format the values, cmap is used to set the color map
#heatmaps are used to show the relationship between two variables, in this case, the average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True, fmt='.1f', cmap='YlGnBu')#showing the average arrival delay for each airline by month using a heatmap
plt.xlabel('Month', fontsize=14)
plt.ylabel('Airline', fontsize=14)
plt.show()