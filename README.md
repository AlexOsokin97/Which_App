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

***This barplot represents all the categories with apps above 1 billion download. As you can see, the top category with 18 apps with over 1 billion downloads is Communication followed by Social with 8 apps and Game with 7 apps. This plot although basic gives us alot of information to which category your app should be related. In addition this plot also gives us information that even in the modern age with computers, laptops and smartphones being on our side 24/7, we still love communicate and sociallize with each other***


![alt text][plot2] 

***With the help of the barplot I managed to get information about the average app rating among the popular apps. The reason I wanted to acquire that information was to see whether those apps are also of a high quality. The distribution plot helped me to gain a rating's frequency among the popular apps and also that there were some unusual apps with rating below 4.0***  

[plot1]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/billioninstalls.png "billioninstalls"
[plot2]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/popularapps.png "Popular Apps"

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
