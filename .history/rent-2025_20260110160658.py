import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('datasets/housing.csv')

#print(df.head(10))

#the goal is to predict medium_house_value (target)
#the other variables are input variables

#drops nan values and save it in the data object
df.dropna(inplace=True)
#print(df.info())

#train the model with part of the data e evaluate with the other part of the data
from sklearn.model_selection import train_test_split

#x is the data frame without the target variable (features)

x = df.drop(['median_house_value'], axis= 1)
y = df['median_house_value']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)