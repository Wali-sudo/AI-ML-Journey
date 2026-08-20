#selecting data for modeling

import pandas as pd

melbourne_data=pd.read_csv('/home/waliahmad/Downloads/melb_data.csv')
print(melbourne_data.columns)#columns of the dataset


melbourne_data = melbourne_data.dropna(axis=0)#dropping rows with missing values

#selecting the target and features for modeling
y=melbourne_data.Price#this is the target variable we want to predict
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']#these are the features we will use to predict the target variable
x=melbourne_data[melbourne_features]#this is the data we will use to train the model

print(x.describe())#summary statistics of the features

from sklearn.tree import DecisionTreeRegressor#this is the model we will use to predict the target variable
model = DecisionTreeRegressor(random_state=1)#creating an instance of the model,random_state is used to ensure that the results are reproducible,1 means that the random number generator will produce the same results every time the code is run
model.fit(x, y)#training the model with the features and target variable

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(model.predict(x.head()))