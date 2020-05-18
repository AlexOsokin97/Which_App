# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:05:20 2020

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#Loading the Dataset 
data = pd.read_csv('ML_df.csv')

#creating a copy of the data set
df = data.copy()

#Dropping the irrelevant columns
df.drop(['Unnamed: 0', 'App', 'Last Updated', 'numeric_date'], axis=1,inplace=True)







