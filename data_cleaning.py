# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:37:28 2020

@author: Alexander
"""
import numpy as np
import pandas as pd
import math

#importing the dataset
df_apps = pd.read_csv('./Original/googleplaystore.csv')

#creating a series of nans in each column
sum_nans = df_apps.isna().sum()

#cleaning the data:
df_apps_clean = df_apps.copy()

#Dropping irrelavent columns
df_apps_clean.drop(['Current Ver','Android Ver'],axis=1, inplace=True)
df_apps_clean.drop(['App', 'Genres'],axis=1, inplace=True)

#CATEGORY:
i = df_apps_clean[(df_apps_clean.Category == '1.9')].index
df_apps_clean.drop(i, inplace=True)
df_apps_clean['Category'] = df_apps_clean['Category'].astype('category')

#REVIEWS:
df_apps_clean['Reviews'] = pd.to_numeric(df_apps_clean['Reviews'])

#TYPE:
df_apps_clean['Type'] = df_apps_clean['Type'].astype('category')

#Price:
df_apps_clean['Price'] = df_apps_clean['Price'].str.replace('$', '')
df_apps_clean['Price'] = pd.to_numeric(df_apps_clean['Price'])

#CONTENT RATING:
df_apps_clean['Content Rating'] = df_apps_clean['Content Rating'].str.replace('[\d+,+]', '')
df_apps_clean['Content Rating'] = df_apps_clean['Content Rating'].astype('category')

#SIZE:
df_apps_clean['Size'] = df_apps_clean['Size'].apply(lambda x: -1 if x == 'Varies with device' else x)
df_apps_clean['Size'] = df_apps_clean['Size'].str.replace('[M, k]', '')
df_apps_clean['Size'] = pd.to_numeric(df_apps_clean['Size'])

#INSTALLS:
df_apps_clean['Installs'] = df_apps_clean['Installs'].str.replace('[, +]', '')
df_apps_clean['Installs'] = pd.to_numeric(df_apps_clean['Installs'])





#and importing knn imputer to fill the nan values 
tst = df_apps_clean.copy()

categorical_feature_mask = tst.dtypes=='category'
# filter categorical columns using mask and turn it into a list
categorical_cols = tst.columns[categorical_feature_mask].tolist()

# import labelencoder
from sklearn.preprocessing import LabelEncoder
# instantiate labelencoder object
le = LabelEncoder()
# apply le on categorical feature columns
tst[categorical_cols] = tst[categorical_cols].apply(lambda col: le.fit_transform(col))











#importing KNN imputer
#using different types of k for later testing
#from sklearn.impute import KNNImputer
#imputer = KNNImputer(n_neighbors=33)
#df_filled = imputer.fit_transform(tst)

#array to df
#ML_df = pd.DataFrame(data=df_filled)

# K = 67
#imputer2 = KNNImputer(n_neighbors=67)
#df2_filled = imputer2.fit_transform(tst)

#ML_df2 = pd.DataFrame(data=df2_filled)

#saving to csv:
#df_apps_clean.to_csv('C:/Users/User/Documents/GitHub/Which_App_Category/EDA_df.csv')
#ML_df.to_csv('C:/Users/User/Documents/GitHub/Which_App_Category/Model_df.csv')
#ML_df2.to_csv('C:/Users/User/Documents/GitHub/Which_App_Category/Model2_df.csv')
