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

#finding the median size of each app category
size_medians = df_apps_clean.groupby('Category')['Size'].median()

#INSTALLS:
df_apps_clean['Installs'] = df_apps_clean['Installs'].str.replace('[, +]', '')
df_apps_clean['Installs'] = pd.to_numeric(df_apps_clean['Installs'])


#RATING:
#finding the median rating for each category
rating_medians = df_apps_clean.groupby(['Category'])['Rating'].median()

#creating a copy of the data set, setting dummy variables for the categorical data 
#and importing knn imputer to fill the nan values 
tst = df_apps_clean.copy()
tst = pd.get_dummies(tst, columns=["Category", "Content Rating", "Type"])
tst.drop("Last Updated",axis=1, inplace=True)

#importing KNN imputer
#using different types of k for later testing
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=33)
df_filled = imputer.fit_transform(tst)

#array to df
ML_df = pd.DataFrame(data=df_filled)

# K = 17
imputer1 = KNNImputer(n_neighbors=17)
df1_filled = imputer1.fit_transform(tst)

ML_df1 = pd.DataFrame(data=df1_filled)

# K = 67
imputer2 = KNNImputer(n_neighbors=67)
df2_filled = imputer2.fit_transform(tst)

ML_df2 = pd.DataFrame(data=df2_filled)

# K = 105
imputer3 = KNNImputer(n_neighbors=105)
df3_filled = imputer3.fit_transform(tst)

ML_df3 = pd.DataFrame(data=df3_filled)
#saving to csv:
df_apps_clean.to_csv('C:/Users/User/Documents/GitHub/Which_App_Category/EDA_df.csv')
ML_df.to_csv('C:/Users/User/Documents/GitHub/Which_App_Category/Model_df.csv')
ML_df1.to_csv('C:/Users/User/Documents/GitHub/Which_App_Category/Model1_df.csv')
ML_df2.to_csv('C:/Users/User/Documents/GitHub/Which_App_Category/Model2_df.csv')
ML_df3.to_csv('C:/Users/User/Documents/GitHub/Which_App_Category/Model3_df.csv')
