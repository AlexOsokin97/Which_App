# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 01:06:17 2020

@author: Alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_data(path):
    data = pd.read_csv(path+'.csv')
    return data

def get_columns(data):
    cols = data.columns
    return cols
    
def drop_columns(data,columns):
    new_data = data.copy()
    new_data.drop(labels=columns, axis=1, inplace=True)
    return new_data


data = get_data('ML_df') 
cols = get_columns(data)
cols_drop = ['Unnamed: 0', 'App', 'Genres', 'Last Updated', 'numeric_date']
new_data = drop_columns(data, cols_drop)

for indx, col in enumerate(cols):
    print(indx, col)
    
new_data = new_data.loc[(new_data['Reviews'] < 10000000) & (new_data['Price'] < 50) & (new_data['updated'] < 2000) & 
                        (new_data['Rating'] > 1.5) & (new_data['Installs'] < 200000000)]


dums = pd.get_dummies(new_data)

X = dums.drop(labels=['Rating', 'Category_WEATHER', 'Content Rating_Teen'], axis=1).values
y = dums['Rating'].values













