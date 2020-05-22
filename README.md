# Project Overview:
* **This project focuses on helping developers to create popular high rated apps**
* **Used over 10,000 app samples**
* **Used exploritory data analysis to give my data an initial cleaning**
* **Explored the data by ploting barplots, violinplots, pieplots and many more**
* **Researched deeper into the dataset i.e: found the most expesive app, which are the most famous apps.**
* **Cleaned and preprocessed the data for the model usage**
* **Trained and tested 3 different Artificial Neural Networks models to predict app's rating**

## Code & Resources:
* **Python Version**: 3.8.2
* **Original Data Set:** [Here](https://www.kaggle.com/lava18/google-play-store-apps#googleplaystore.csv)
* **Packages:** pandas, numpy, matplotlib, seaborn, scipy
* **IDES Used:** Anaconda, Spyder, Jupyter-Notebook, Jupyter-Lab
* **Related plotting examples:** [kaggle](https://www.kaggle.com/tanetboss/how-to-get-high-rating-on-play-store)
* **Statistical Hypothesys Testing** [Here](https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/)
* **Activation Functions:** [Here](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)
* **Loss Functions:** [Here](https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/)

## Data Cleaning:
* **Created a copy of the original dataset**
* **Removed irrelavant columns**
* **Transformed columns into numerical data by removing special characters**
* **Used time series transformation inorder to see how many days have passed**
* **Created new columns by combining correlated data**

# EDA:
**One of the most intresting parts in this project. I explored the data by applying a big variaty of plots and graphs, used regression plots to find correlation between variables. I also used pandas to clean and manipulate the data in order to gain more information and to make it more easy to extract and use. Here are some examples from my analysis advanture:**

![alt text][plot1] 
![alt text][plot2]
![alt text][plot3] 

[plot1]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/billioninstalls.png "billioninstalls"
[plot2]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/regplots.png "regplots"
[plot3]: https://github.com/AlexOsokin97/Which_App_Category/blob/master/Data%20Analysis/pngs/popularapps.png "Popular Apps"

# Model Building:
**In this project I decided to use an Artificial Neural Network models. Neural Networks are very powerful models which can give high rated results so, I wanted to see how they'll preform on this dataset.**
* **The model was trained to predict the app's rating according to 39 different features**
* **Used panda's "get_dummies" function in order to get a numerical representation of the categorical data**
* **Applied Standardization for feature scalling**
* **Created a training and testing sets (7000+ samples for training & 2000+ samples for testing)**
* **I initialized 3 NN models with different amount of layers. Different activation, optimization, loss and evaluation matrices functions.**
* **Created variables that stored each model's loss and mse preformance on the training and testing data**
* **Finally, I created 3 different plots for each model to see how quickly and how well it took to each model to converge when it was used on the training and testing sets**

# The Models:
**In my model building process I built 3 different Artificial Neural Networks:**

## Model 1:

<img src="https://github.com/AlexOsokin97/Which_App_Category/blob/master/ANN/models%20svg/nn.svg">
 
* Layers: 39 neurons in input_layer, 4X20 neurons in hidden_layers, 1 neuron in output_layer. 
* Activation Functions: input and hidden layers: **ReLU** , Output layer: **Linear**. 
* Optimizer: **AdaGrad** 
* Loss_function: **mean_squared_logarithmic_error** 
* Metrics_function: **mse** 

## Model 2:

<img src="https://github.com/AlexOsokin97/Which_App_Category/blob/master/ANN/models%20svg/nn1.svg">

* Layers: 39 neurons in input_layer, 2X20 neurons in hidden_layers, 1 neuron in output_layer. 
* Activation Functions: input and hidden layers: **ReLU** , Output layer: **Linear**. 
* Optimizer: **Gradient Descent** 
* Loss_function: **mean_squared_error** 
* Metrics_function: **mse**

## Model 3:

<img src="https://github.com/AlexOsokin97/Which_App_Category/blob/master/ANN/models%20svg/nn2.svg">

* Layers: 39 neurons in input_layer, 6X20 neurons in hidden_layers, 1 neuron in output_layer. 
* Activation Functions: input and hidden layers: **ReLU** , Output layer: **Linear**. 
* Optimizer: **Gradient Descent** 
* Loss_function: **mean_absolute_error** 
* Metrics_function: **mse**
