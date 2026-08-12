import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris_data=pd.read_csv('/home/waliahmad/Downloads/iris.csv',index_col=0)#reading the iris data from the csv file
print(iris_data.head())
print(iris_data.tail())
#histogram is used to show the distribution of a continuous variable
plt.figure(figsize=(10, 6))
plt.title("Histogram of Sepal Length")
#syntax for histogram is sns.histplot(data=dataframe, x=column_name, bins=number_of_bins, kde=True), kde is used to show the kernel density estimate
sns.histplot(data=iris_data, x='Sepal Length (cm)', bins=20, kde=True)#showing the distribution of sepal length using a histogram
plt.xlabel("Sepal Length")
plt.ylabel("Count")
plt.show()

#KDE plot is used to show the distribution of a continuous variable
plt.figure(figsize=(10, 6))
plt.title("KDE Plot of Sepal Length")
#syntax for KDE plot is sns.kdeplot(data=dataframe, x=column_name, fill=True), fill is used to fill the area under the curve
sns.kdeplot(data=iris_data, x='Sepal Length (cm)', fill=True)#showing the distribution of sepal length using a KDE plot
plt.xlabel("Sepal Length")
plt.ylabel("Density")
plt.show()

#2D KDE plot is used to show the distribution of two continuous variables
plt.figure(figsize=(10, 6))
plt.title("2D KDE Plot of Sepal Length and Sepal Width")
#syntax for 2D KDE plot is sns.kdeplot(data=dataframe, x=column_name, y=column_name, fill=True), fill is used to fill the area under the curve
sns.kdeplot(data=iris_data, x='Sepal Length (cm)', y='Sepal Width (cm)', fill=True)#showing the distribution of sepal length and sepal width using a 2D KDE plot
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

#we can also use hue to show the distribution of a continuous variable for different categories in histogram, KDE plot and 2D KDE plot