#There are 3 approaches for handling missing values
#1) drop the column
#2) imputation(filling missing values with some number), like we can add mean in place of missing values
#3) In this approach, we impute the missing values, as before. And, additionally, for each column with missing entries in the original dataset, we add a new column that shows the location of the imputed entries.

import pandas as pd
from sklearn.model_selection import train_test_split

melbdata=pd.read_csv('/home/waliahmad/Downloads/melb_data.csv')
y=melbdata.Price
filtered_data=melbdata.drop(['Price'],axis=1)
#used drop instead of dropna cuz drop is used to drop as column while dropna drop the whole row containing useful information as well
x = filtered_data.select_dtypes(exclude=['object'])
#select datatypes is a function used to filter DataFrame columns based on their data types
#exclude=['object'] tells Pandas: "Remove all string/text columns and return only numerical ones (integers and floats)
X_train, X_valid, y_train, y_valid = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=0)