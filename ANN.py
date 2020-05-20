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
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

#Encoding the categorical data
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#preprocessing X with columntransformer and onehot encoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [5])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
X[: , :3] = X[:, :3].astype('int64')
X = np.delete(X, [2],axis=1)

#preprocessing y with labelencoder
encoder = LabelEncoder()
y = encoder.fit_transform(y)

#splitting the data into training and testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#applying feature scaling (not on Rating)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train[:, [3, 4, 5, 6, 8]] = scaler.fit_transform(X_train[:, [3, 4, 5, 6, 8]])
X_test[:, [3, 4, 5, 6, 8]] = scaler.transform(X_test[:, [3, 4, 5, 6, 8]])

#importing keras libraries and packages for the NN model
import keras
from keras.models import Sequential 
from keras.layers import Dense

#initializing the ANN
neural = Sequential()

#creating NN input layer
neural.add(Dense(output_dim = 5, init = 'uniform', activation = 'relu', input_dim = 9))

#creating the NN hidden layers
neural.add(Dense(output_dim = 5, init = 'uniform', activation = 'relu', input_dim = 5))
neural.add(Dense(output_dim = 5, init = 'uniform', activation = 'relu', input_dim = 5))
neural.add(Dense(output_dim = 5, init = 'uniform', activation = 'relu', input_dim = 5))
neural.add(Dense(output_dim = 5, init = 'uniform', activation = 'relu', input_dim = 5))
neural.add(Dense(output_dim = 5, init = 'uniform', activation = 'relu', input_dim = 5))

#creating NN output layer
neural.add(Dense(output_dim = 33, init = 'uniform', activation = 'softmax', input_dim = 5))

#compiling the ANN (using stochastic gradient descent)
neural.compile(optimizer = 'adam', loss='categorical_crossentropy', metrics=['accuarcy'])

