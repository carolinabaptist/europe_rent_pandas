import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('datasets/housing.csv')

print(df.head(10))
print(df.info())
print(df.describe())
