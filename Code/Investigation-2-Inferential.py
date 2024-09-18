# Load packages that will potentially be used.
import numpy as np
import math
import scipy
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets.
db2 = pd.read_csv('C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT140/HIT140 Assignment 2/Code/dataset2.csv')
db3 = pd.read_csv('C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT140/HIT140 Assignment 2/Code/dataset3.csv')

# Merge the dataframes based on the 'ID'.
df = pd.merge(db3, db2, on='ID', how='inner')

# Create a new column T_hours which combines T_wk and T_we columns.
df['T_hours'] = df['T_wk'] + df['T_we']

# Filter the dataset where Usef, Thcklr, and Dealpr are less than or equal to 3.
filtered_df = df[(df['Usef'] <= 3) & (df['Thcklr'] <= 3) & (df['Dealpr'] <= 3)]

#Regression Analysis.
X = filtered_df[['Usef', 'Thcklr', 'Dealpr']]
y = filtered_df['T_hours']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
y_pred = model.predict(X)

#Sccaterplot to display the data.
plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel('Actual T_hours')
plt.ylabel('Predicted T_hours')
plt.title('Actual vs Predicted T_hours')
plt.show()