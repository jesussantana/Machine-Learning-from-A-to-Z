# Missing Data

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('/content/machinelearning-az/datasets/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Data.csv')
X = df.iloc[:, -1].values
y = dataset.iloc[:, 3].values

# Tratamiento de los NAs

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy = "mean", verbose=0)
imputer = imputer.fit(X[:,1:3]) 
X[:, 1:3] = imputer.transform(X[:,1:3])