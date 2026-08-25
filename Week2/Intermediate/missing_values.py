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

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Get names of columns with missing values
cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]#any()checks whether at least one element in an iterable evaluates to Tru

# Drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

print("MAE from Approach 1 (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

from sklearn.impute import SimpleImputer

# Imputation
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
#fit calculate the mean and transform replace missing value with it 
#SimpleImputer outputs a raw NumPy array, so wrapping it in pd.DataFrame() converts it back into a Pandas DataFrame.

imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
#Never call .fit() on validation/test data. Using training means prevents data leakage (where the model accidentally gets hints about the test set).

# Imputation removed column names; put them back
#When Scikit-Learn tools process data, they temporarily convert Pandas objects into raw numerical matrices.
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

print("MAE from Approach 2 (Imputation):")
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))


# Make copy to avoid changing original data (when imputing)
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()

# Make new columns indicating what will be imputed
for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

# Imputation
my_imputer = SimpleImputer()
imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(my_imputer.transform(X_valid_plus))

# Imputation removed column names; put them back
imputed_X_train_plus.columns = X_train_plus.columns
imputed_X_valid_plus.columns = X_valid_plus.columns

print("MAE from Approach 3 (An Extension to Imputation):")
print(score_dataset(imputed_X_train_plus, imputed_X_valid_plus, y_train, y_valid))

