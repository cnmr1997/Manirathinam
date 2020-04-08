# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:08:27 2020

@author: MANIRATHNAM
"""

# Simple Linear Regression
# Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the Dataset
mydataset = pd.read_csv('Salary_Data.csv')
X = mydataset.iloc[:, :1].values
y = mydataset.iloc[:, 1].values

# Splitting the Dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 1/3,random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Visualising the training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train),color = 'blue')
plt.title('Salary vs Experience(Training Set)')
plt.xlabel('years of Experience')
plt.ylabel('Salary')
plt.show()


# Visualising the test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train),color = 'blue')
plt.title('Salary vs Experience(Test Set)')
plt.xlabel('years of Experience')
plt.ylabel('Salary')
plt.show()