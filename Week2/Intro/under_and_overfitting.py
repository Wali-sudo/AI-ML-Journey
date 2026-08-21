#overfitting occur when model perform well on the train data but perform poorly on the testing data,solve it by adjusting tree depth
#underfitting is when model perform poor even on the training data,solve it by increasing the tree depth

import pandas as pd
from sklearn.tree import DecisionTreeRegressor  
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def get_mae(leaf, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=leaf, random_state=0)
    model.fit(train_X, train_y)
    pred_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, pred_val)
    return mae

melb_data = pd.read_csv('/home/waliahmad/Downloads/melb_data.csv')
filtered_melb_data = melb_data.dropna(axis=0)

y = filtered_melb_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
x = filtered_melb_data[melbourne_features]

train_X, val_X, train_y, val_y = train_test_split(x, y, random_state=0)

for i in [5, 50, 500, 5000]:
    my_mae = get_mae(i, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" % (i, my_mae))