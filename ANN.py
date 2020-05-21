# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:05:20 2020

@author: Alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loading the Dataset 
data = pd.read_csv('ML_df.csv')

#creating a copy of the data set
df = data.copy()

#Dropping the irrelevant columns
df.drop(['Unnamed: 0', 'App', 'Last Updated', 'numeric_date', 'Genres'], axis=1,inplace=True)

#creating X, y
X = df.iloc[:, [0,2,3,4,5,6,8]]
y = df.iloc[:, 1]

#Encoding the categorical data with dummy variables
X = pd.get_dummies(X, columns=["Category", "Content Rating"], prefix=["catgry", "cr"])
X.drop(labels=["catgry_ART_AND_DESIGN","cr_Everyone"], axis=1, inplace=True)
X = X.values
y = y.values

#splitting the data into training and testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

#applying feature scaling 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train[:, 0:5] = scaler.fit_transform(X_train[:, 0:5])
X_test[:, 0:5] = scaler.transform(X_test[:, 0:5])

#importing keras libraries and packages for the NN model
import keras
from keras.models import Sequential 
from keras.layers import Dense

#initializing the ANN
neural = Sequential()

#creating NN input layer
neural.add(Dense(activation="relu", input_dim=39, units=20, kernel_initializer="normal"))

#creating the NN hidden layers
neural.add(Dense(activation="relu" , input_dim=20, units=20, kernel_initializer="normal"))
neural.add(Dense(activation="relu" , input_dim=20, units=20, kernel_initializer="normal"))
neural.add(Dense(activation="relu" , input_dim=20, units=20, kernel_initializer="normal"))

#creating NN output layer
neural.add(Dense(activation="linear", input_dim=20, units=1, kernel_initializer="normal"))

#compiling the ANN
neural.compile(optimizer = 'sgd', loss='mse', metrics=['mae'])

#fitting the model
neural.fit(X_train, y_train, batch_size=10, nb_epoch=100)

y_predict = neural.predict(X_test)


