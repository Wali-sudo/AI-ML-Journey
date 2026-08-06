#kaggle
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
spotify_data = pd.read_csv('/home/waliahmad/Downloads/most_streamed_spotify_2025.csv')
print(spotify_data.head())
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
plt.show()
