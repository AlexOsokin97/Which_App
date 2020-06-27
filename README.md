# Project Overview:
***Are you a developer who has an idea for a new app but not sure how successful it would be?***

**Nowadays, in the 21th century with a booming development industry it is hard to come up with a new idea for an app/software. Have you ever searched for a specific app in app store or apple store and saw a large amount of apps with the same concept?**

**Unlike in the 20th century, when the field of software development was still making its first steps and smart phones weren't even invented yet it was hard to a random person with an idea to sit down and with ease fulfill his vision. This is because in the past computational power wasn't as advanced and cheap as it's today and you would most like needed to have a degree in the field of computer science. But today, with fast and easy accessible information, with thousands of different courses online everyone can learn and develop anything they want.**

**In this project I am ought to give developers a quick tour on the app market and predict the rating of their future app by the necessary features that they'll need to provide. How?  By using a dataset with 10,000 different apps from different categories, cleaning and remodeling the data, exploring the dataset by creating complex graphs and plots which explain every feature and show correlation between them and training a Machine Learning model which uses many app related features to predict an app's rating** 

## Data Cleaning & Exploratory Data Analysis:
***After getting the data and exploring it a bit, it was time to start the cleaning phase. Data comes in all shapes and sizes and 99% of the time it the doesn't come in a form you want it to be.***

**I started out the cleaning process by firstly creating a copy of the original dataset and finding how many NaN values were there in each column and the precentage. Secondly, I dropped the columns which contained too much missing data. Thirdly, I used statistical methods such as mean and median to replace missing values and correlation matrix to find which columns were valuable and which were useless (for my case). Finally, I used lambda functions to transform the columns to their right data type (int, string) by removing unrelated information.**

**Finally, when the cleaning part was over the next phase was exploritory data analysis in which, I explored the data by creating variaty of plots and graphs, used regression plots to visualize the correlation between features. Here are some examples from my analysis advanture:**

![alt text][plot1] 

***This barplot represents all the categories with apps above 1 billion download. As you can see, the top category with 18 apps with over 1 billion downloads is Communication followed by Social with 8 apps and Game with 7 apps. This plot although basic gives us alot of information to which category your app should be related. In addition this plot also gives us information that even in the modern age with computers, laptops and smartphones being on our side 24/7, we still love communicate and sociallize with each other.***


![alt text][plot2] 

***With the help of the barplot I managed to get information about the average app rating among the popular apps. The reason I wanted to acquire that information was to see whether those apps are also of a high quality. The distribution plot helped me to gain a rating's frequency among the popular apps and also that there were some unusual apps with rating below 4.0.***  

[plot1]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/billioninstalls.png "billioninstalls"
[plot2]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/popularapps.png "Popular Apps"

# Model Building & Performance:
***Does the data has enough information and features to accuratly predict an app's rating?***

***After getting the data, cleaning, remodeling and exploring it with statistics and visualization plots it was time to check if a machine learning model could succefully predict an app's rating.***

**The first step I did was to remove outliers from the data because outliers are unusual and rare observations in other words, they are unique occurrences and have a very slim chance of happening again so I did not want them to affect my model.**

* Removal of outliers: There are many methods to remove outliers. I decided to create scatter plots for each feature which could have outliers and assigned a threshold with the max value each observation could have (value which is > max = outlier). The maximum value was decided after looking at the area where most of the data points were scattered

**The second step was encoding the categorical data into 1's|0's. Because there were many categories I ended up with a dataset with more columns where the new columns consisted of 1 and 0 values to indicate whether a category was present in the observation.**

* Encoding method: I used the pandas built in function pandas.get_dummies which transforms each value in a categorical column to a new column with values of 1 and 0.

**The third step was importing model selection packages which would help me optimize and tune my models to get better results. I used the following packages:**

* *train_test_split:* This package takes your data and splits it to train data and testing data. I used this package in order to create a dataset for a model to learn from and a data set to test the model in order to check how well the model performed. ***In this project I split the data into 80% training set and 20% testing set***

* *cross_val_score:* This package uses your model to test it how well it performes on the dataset by taking the dataset and splits it to K folds where K-1 folds are used for training and 1 fold for testing. It splits the dataset until all possible combinations are done. ***I used 10-fold cross validation***

* *grid_search_cv:* This package allows parameter tuning of a model and testing each combination on K folds and picking the best one. ***In my case I used 5 fold split***

**The forth step was to choose the scoring metric to see each model's performance on the training set and on the testing set.**

* *mean_absolute_error:* This metric gives the average magnitude of the errors a set of predictions without considering their direction.

**In this step I created 5 functions each for different purpose and would be used by every model. The functions are:**

* *naive_model:* which fits the given model into cross_val_score and returns the average score of K scores

* *complex_model:* which fits the given model into GridSearchCV and returns the params of the best model and the score of that model

* *save_model:* a function that saves a given model using pickle package into a a .sav file

* *model_performance:* which uses a given model's predict function to predict the Rating of the unseen data and then evaluating the outcome using mean_absolute_error metric

* *feature_scaling:* a functions which scales given features using a user provided method.

# Code & Resources:
* **Python Version**: 3.8.2
* **Original Data Set:** [Here](https://www.kaggle.com/lava18/google-play-store-apps#googleplaystore.csv)
* **Packages:** pandas, numpy, matplotlib, seaborn, scipy, sklearn, keras
* **IDES Used:** Anaconda, Spyder, Jupyter-Notebook, Jupyter-Lab
* **Related plotting examples:** [kaggle](https://www.kaggle.com/tanetboss/how-to-get-high-rating-on-play-store)
* **Statistical Hypothesys Testing** [Here](https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/)
* **Activation Functions:** [Here](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)
* **Loss Functions:** [Here](https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/)
* **Create NN Diagrams:** [Here](http://alexlenail.me/NN-SVG/index.html)
