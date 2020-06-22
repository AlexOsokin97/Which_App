# Project Overview:
***Are you a developer who has an idea for a new app but not sure how successful it would be?***

**Nowadays, in the 21th century with a booming development industry it is hard to come up with a new idea for an app/software. Have you ever searched for a specific app in app store or apple store and saw a large amount of apps with the same concept?**

**Unlike in the 20th century, when the field of software development was still making its first steps and smart phones weren't even invented yet it was hard to a random person with an idea to sit down and with ease fulfill his vision. This is because in the past computational power wasn't as advanced and cheap as it's today and you would most like needed to have a degree in the field of computer science. But today, with fast and easy accessible information, with thousands of different courses online everyone can learn and develop anything they want.**

**In this project I am ought to give developers a quick tour on the app market and predict the rating of their future app by the necessary features that they'll need to provide. How?  By using a dataset with 10,000 different apps from different categories, cleaning and remodeling the data, exploring the dataset by creating complex graphs and plots which explain every feature and show correlation between them and training a Machine Learning model which uses many app related features to predict an app's rating** 

## Data Cleaning & Exploratory Data Analysis:
* **Created a copy of the original dataset**
* **Removed irrelavant columns**
* **Transformed columns into numerical data by removing special characters**
* **Used time series transformation inorder to see how many days have passed**
* **Created new columns by combining correlated data**

**One of the most intresting parts in this project. I explored the data by applying a big variaty of plots and graphs, used regression plots to find correlation between variables. I also used pandas to clean and manipulate the data in order to gain more information and to make it more easy to extract and use. Here are some examples from my analysis advanture:**

![alt text][plot1] 
![alt text][plot2]
![alt text][plot3] 

[plot1]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/billioninstalls.png "billioninstalls"
[plot2]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/regplots.png "regplots"
[plot3]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/popularapps.png "Popular Apps"

# Model Building & Performance:


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
