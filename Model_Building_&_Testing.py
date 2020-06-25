# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 03:16:03 2020

@author: Alexander
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

new_data = new_data.loc[(new_data['Reviews'] < 10000000) & (new_data['Price'] <= 20) & (new_data['updated'] < 2000) &
                        (new_data['Rating'] > 1.5) & (new_data['Installs'] < 200000000)]

dums = pd.get_dummies(new_data)
dums.head()

X = dums.drop(labels=['Rating', 'Category_WEATHER', 'Content Rating_Teen'], axis=1).values
y = dums['Rating'].values

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import pickle

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

def naive_model(model, training_features, training_label, scoring, cv):
    avg_score = np.mean(cross_val_score(model, training_features, y=training_label, scoring=scoring, cv=cv))
    return avg_score

def complex_model(model, training_features, training_label, params, scoring, cv):
    grid_search = GridSearchCV(model, param_grid=params, scoring=scoring, cv=cv)
    grid_search.fit(training_features, training_label)
    best_find = grid_search.best_estimator_
    best_score = grid_search.best_score_
    return best_find, best_score

def save_model(model, name):
    filename = name+".sav"
    pickle.dump(model, open(filename, 'wb'))
    
def model_performance(filename,testing_features, testing_label):
        loaded_model = pickle.load(open(filename, 'rb'))
        y_pred = loaded_model.predict(testing_features)
        accuracy = mean_absolute_error(testing_label,y_pred)
        return accuracy
    
def feature_scaling(training_features, testing_features, train_cols, test_cols, method):
    training_features[:, train_cols] = method.fit_transform(training_features[:, train_cols])
    testing_features[:, test_cols] = method.transform(testing_features[:, test_cols])
    return training_features, testing_features

###########################################################################################

rf_reg = RandomForestRegressor()

cvs_ = naive_model(rf_reg, X_train, y_train,'neg_mean_squared_error', 10)
print("Average MSE is: ", cvs_)

rf_reg_params = [{'n_estimators':range(50,150,50), 'criterion':('mse','mae'), 'max_depth': range(1,16,1),
                  'min_samples_split': range(10,100,20), 'min_samples_leaf': range(1,10,1), 
                  'max_features':('auto', 'sqrt', 'log2')}]

best_rf_reg_model, best_rf_reg_score = complex_model(rf_reg, X_train, y_train, rf_reg_params, 'neg_mean_squared_error', 3)

print("best estimator's score is: ",best_rf_reg_score)

save_model(best_rf_reg_model, 'rf_reg')

###########################################################################################

lm_l = Lasso()

np.mean(cross_val_score(lm_l,X_train,y_train,scoring='neg_mean_squared_error', cv=10))

lasso_alpha = [{'alpha':(0.1,0.2,0.3,0.4,0.5, 0.6, 0.7, 0.8, 0.9, 1.0)}]

best_lasso_model, best_lasso_score = complex_model(lm_l, X_train, y_train, lasso_alpha, 'neg_mean_squared_error', 3)

print("best estimator's score is: ", best_lasso_score)

save_model(best_lasso_model, 'lasso_reg')

###########################################################################################

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train,scoring='neg_mean_squared_error', cv=10))

save_model(lm, 'linear_model')

###########################################################################################

svr_m = SVR(kernel='linear')

sc = StandardScaler()
X_train_norm, X_test_norm = feature_scaling(X_train, X_test, [0, 1, 2, 5], [0,1,2,5], sc)

np.mean(cross_val_score(svr_m,X_train_norm,y_train,scoring='neg_mean_squared_error', cv=10))



###########################################################################################

rf_evalu = model_performance('', X_test, y_test)
print("Performance on unseen data (RandomForest): ", )

lasso_evalu = model_performance('lasso_reg.sav', X_test, y_test)
print("Performance on unseen data (Lasso): ", lasso_evalu)

linear_model_evalu = model_performance('linear_model.sav', X_test, y_test)
print("Performance on unseen data (LinearRegression): ", linear_model_evalu)


















