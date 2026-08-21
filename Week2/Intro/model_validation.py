import pandas as pd
melb_data=pd.read_csv('/home/waliahmad/Downloads/melb_data.csv')
filtered_melb_data=melb_data.dropna(axis=0)
y=filtered_melb_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
x=filtered_melb_data[melbourne_features]
from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()
model.fit(x,y)
print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(model.predict(x.head()))


#we will calculate MAE

from sklearn.metrics import mean_absolute_error
predicted_home_prices=model.predict(x)
mae=mean_absolute_error(y,predicted_home_prices)
print(mae)#434.71594577146544




#train and test split


from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(x, y, random_state = 0)
melb_model=DecisionTreeRegressor()
melb_model.fit(train_X, train_y)
val_predictions = melb_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))#265806.91478373145


#as the MAE value before split was 434 and after split is 265806 this indicate that before the split the model was actually memorizing the dataset rather then accurately guessing, after split we came to know that the model was completely blank 


