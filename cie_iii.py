# -*- coding: utf-8 -*-
"""CIE III

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xf8-9nau5hZ820hQBdkzmpwGQ_ra9rty
"""

# @title Data Exploration
import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv('/content/HousingData.csv')

print('First five records :',df.head())
print('Sample statistics :',df.describe())
print('Type of data :',df.isna())

# @title Data Preprocessing
print("Removed the Missing values :",df.dropna())
print("Checking Null values :",df.isnull().sum())
print('Checking missing values :',df.isna().sum())

# @title Data Splitting
x=df[['INDUS','NOX','AGE']]
y=df['RAD']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print('x-train :',x_train)
print('y_train :',y_train)
print('x_test :',x_test)
print('y_test :',y_test)

from sklearn.datasets import load_iris
import pandas as pd

df=pd.read_csv('/content/Iris.csv')

print('Sample data :',df.head())
print('Statistics of dataset :',df.describe())
print('Type of data :',df.info())

# @title Data Preprocessing
print("Removed the Missing values :",df.dropna())
print("Checking Null values :",df.isnull().sum())
print('Checking missing values :',df.isna().sum())

x=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm']]
y=df['PetalWidthCm']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print('x-train :',x_train)
print('y_train :',y_train)
print('x_test :',x_test)
print('y_test :',y_test)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score,mean_squared_error,r2_score,mean_absolute_error

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print('mean_squared_error :',mean_squared_error(y_test,y_pred))
print('r2_score values :',r2_score(y_test,y_pred))
print('Mean absolute Error :',mean_absolute_error(y_test,y_pred))