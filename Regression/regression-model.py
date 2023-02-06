#import dependencies
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error

#load dataset
df_phoenix = pd.read_csv('phoenix_housedata.csv')

##optional: with big enough data set, automatically encode string dtypes##
#label_encoder = LabelEncoder()
#df_phoenix['Subregion']= label_encoder.fit_transform(df_phoenix['Subregion'])

#define variables for model
X = df_phoenix.drop(columns=['Address', 'List Price'])
y = df_phoenix['List Price']

#split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#define model
model = LinearRegression()
model.fit(X, y)

#pass through new values to predict with
prediction = model.predict([[1, 3, 3, 2500]])
print(prediction)

#generate line of best fit and then get the r2_score
linreg = LinearRegression()
linreg.fit(X, y)
linreg.score(X, y)
r2 = linreg.score(X,y)
print(r2)