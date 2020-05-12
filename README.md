# Project Overview:
* **This project focuses on helping app developers choosing the right category for their app development and predicts the popularity of an already existing apps.**
* **Used over 10,000 app samples**
* **Cleaned the data and created 5 datasets. One for exploritory data analysis and four for model fitting (each set has different predicted values by KNN-Imputer).**

## File Description:

## Code & Resources:
* **Python Version**: 3.8.2
* **Original Data Set:** [Here](https://www.kaggle.com/lava18/google-play-store-apps#googleplaystore.csv)
* **Packages:** pandas, numpy, matplotlib, seaborn, sklearn
* **IDES Used:** Anaconda, Spyder, Jupyter-Notebook
* **Missing Data Imputation (KNN):** [Guide](https://medium.com/@amrwrites/knn-based-missing-value-imputation-using-scikit-learn-802fceb5b2ea)
* **Label Encoding:** [Guide](https://pbpython.com/categorical-encoding.html)
* **Calculate Feature Importance:** [Guide](https://machinelearningmastery.com/calculate-feature-importance-with-python/)

# Data Cleaning:
**The Cleaning process of 'googleplaystore.csv' was very challenging and tricky. It contained many categories and for each category there were lots of missing values. I could have just deleted the rows with the missing values but it meant that I would have deleted 1637 rows of data. Altough my dataset contained around 11,000 samples, deleting 1637 meant deleting 13.7% of my whole dataset! And for me that it was alot so I decided to look for a way to fill those missing values. Here's the whole cleaning process:**
* Reading the dataset using Spyder IDE.
* Creating a copy of the dataset and by using pandas created a series with sum of all na values in each column
* Dropping the insignificant columns
* Cleaning the numeric column values by removing special letters and special characters
* Changed each column's data type for the desired type (numeric, categorical)
* Created a copy of the cleaned dataset and applied dummies function for the categorical data.
* Used KNN-Imputation ml algorithm (with different k_neighboors) for filling the missing numeric values.
* Created a dataset for each Knn-algorithm (4) with different k_neighboors and a dataset for exploritory data analysis

# EDA:
