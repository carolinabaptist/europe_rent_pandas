import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('datasets/house-data.xlsx')

#print(df.head(10))
print(df.info())
print(df.describe())
