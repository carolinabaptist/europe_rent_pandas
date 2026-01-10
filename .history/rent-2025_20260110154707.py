import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('datasets/housing.csv')

#print(df.head(10))

#the goal is to predict medium_house_value (target)
#the other variables are input variables

df.dropna()