# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:37:28 2020

@author: Alexander
"""
import numpy as np
import pandas as pd
import math

#importing the dataset
df_apps = pd.read_csv('googleplaystore.csv')

#creating a series of nans in each column
sum_nans = df_apps.isna().sum()

#cleaning the data:
df_apps_clean = df_apps.copy()

#Dropping irrelavent columns
df_apps_clean.drop(['Current Ver','Android Ver','App', 'Genres'],axis=1, inplace=True)

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
df_apps_clean['Content Rating'] = df_apps_clean['Content Rating'].str.replace('[\d+,+]', '').astype('category')
#df_apps_clean['Content Rating'] = df_apps_clean['Content Rating']

#SIZE:
df_apps_clean['Size'] = df_apps_clean['Size'].apply(lambda x: -1 if x == 'Varies with device' else x)
df_apps_clean['Size'] = df_apps_clean['Size'].str.replace('[M, k]', '')
df_apps_clean['Size'] = pd.to_numeric(df_apps_clean['Size'])

#transforming all nan values to 0
#df_apps_clean['Size'] = df_apps_clean['Size'].apply(lambda x: 0 if math.isnan(x) else x)

#finding the median size of each app category
size_medians = df_apps_clean.groupby('Category')['Size'].median()

#INSTALLS:
df_apps_clean['Installs'] = df_apps_clean['Installs'].str.replace('[, +]', '')
df_apps_clean['Installs'] = pd.to_numeric(df_apps_clean['Installs'])

#RATING:
#finding the median rating for each category
rating_medians = df_apps_clean.groupby(['Category'])['Rating'].median()
df_test = df_apps_clean.copy()






