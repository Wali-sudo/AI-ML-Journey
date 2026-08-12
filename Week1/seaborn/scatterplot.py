import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
insurance_data=pd.read_csv('/home/waliahmad/Downloads/insurance.csv')#reading the insurance data from the csv file
print(insurance_data.head())
print(insurance_data.tail())
plt.figure(figsize=(14, 7))
plt.title("Scatterplot of Age vs. Charges")
#syntax for scatterplot is sns.scatterplot(data=dataframe, x=column_name, y=column_name, hue=column_name),hue is used to set the color of the points
sns.scatterplot(data=insurance_data, x='age', y='charges', hue='sex')#showing the relationship between age and charges using a scatterplot, with different colors for male and female
plt.xlabel("Age")
plt.ylabel("Charges")
plt.show()


#for a regression line in scatter plot we use regplot instead of scatterplot, regplot is used to show the relationship between two variables, in this case, age and charges, with a regression line
plt.figure(figsize=(14, 7))
plt.title("Scatterplot of Age vs. Charges with Regression Line")
sns.regplot(data=insurance_data, x='age', y='charges', scatter_kws={'s':10}, line_kws={'color':'red'})#showing the relationship between age and charges using a scatterplot with a regression line, scatter_kws is used to set the size of the points, line_kws is used to set the color of the regression line
plt.xlabel("Age")
plt.ylabel("Charges")
plt.show()


#for colour coding in scatter plot with regression line we use lmplot instead of regplot, lmplot is used to show the relationship between two variables, in this case, age and charges, with a regression line and different colors for male and female
plt.figure(figsize=(14, 7))
plt.title("Scatterplot of Age vs. Charges with Regression Line and Colour Coding")
sns.lmplot(data=insurance_data, x='age', y='charges', hue='sex', scatter_kws={'s':10}, line_kws={'color':'red'})#showing the relationship between age and charges using a scatterplot with a regression line and different colors for male and female, scatter_kws is used to set the size of the points, line_kws is used to set the color of the regression line
plt.xlabel("Age")
plt.ylabel("Charges")
plt.show()  
