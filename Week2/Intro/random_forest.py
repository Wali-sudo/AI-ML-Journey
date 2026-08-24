#random forest consist of multiple decision trees used for both classification and regression and unlike decision trees it take a random subset of data and train a tree on that set then take another subset for next tree this ensure feature randomness, for prediction of regression it take average of all trees output and for classification it goes for majority
import pandas as pd 
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

melb_data=pd.read_csv('/home/waliahmad/Downloads/melb_data.csv')
filtered_melb_data=melb_data.dropna(axis=0)

y=filtered_melb_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
x = filtered_melb_data[melbourne_features]

train_x,val_x,train_y,val_y=train_test_split(x,y,random_state=0)

model=RandomForestRegressor(n_estimators=1000,random_state=0)#another parameter criterion is used which determines how each decision tree inside the forest measures split quality when building its branches.
#squared_error: Squares the errors, which heavily penalizes large mistakes. Outliers (e.g., a single $10,000,000 mansion) will pull the tree's split points toward them.
#absolute_error: Treats all errors linearly. Outliers have a much smaller effect on the tree's splits, making the model more robust to noisy data.
model.fit(train_x,train_y)
pred_val=model.predict(val_x)
my_mae=mean_absolute_error(val_y,pred_val)
print(my_mae)