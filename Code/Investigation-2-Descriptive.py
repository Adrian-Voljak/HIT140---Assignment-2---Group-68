#Load packages that will potentially be used.
import numpy as np
import math
import scipy
import statsmodels
import pandas as pd
import matplotlib.pyplot as plt

#Load datasets.
db2 = pd.read_csv('C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT140/HIT140 Assignment 2/Code/dataset2.csv')
db3 = pd.read_csv('C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT140/HIT140 Assignment 2/Code/dataset3.csv')

#Creating a function to calculate upper bound using IQR.
def calculate_upper_bound(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    return upper_bound

#Calculate upper bounds for each column in dataset2.
columns_of_interest = ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']
upper_bounds = {}
for col in columns_of_interest:
    if col in db2.columns:
        upper_bounds[col] = calculate_upper_bound(db2[col])

#Filter dataset2 to find IDs that meet or exceed the upper bounds.
meeting_ids = set()
for col, bound in upper_bounds.items():
    meeting_ids.update(db2[db2[col] >= bound]['ID'])

#Define which columns need checking.
columns_to_check = ['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 'Thcklr', 'Goodme', 'Clsep', 'Conf', 'Mkmind', 'Loved', 'Intthg', 'Cheer']

#Filter dataset3 to find IDs where all specified columns have values of 3 or below.
filtered_dataset3 = db3[(db3[columns_to_check] <= 3).all(axis=1)]

#Get the set of IDs that meet this condition.
dataset3_ids = set(filtered_dataset3['ID'])

#Find common IDs that are in both meeting_ids and dataset3 ids.
common_ids = meeting_ids.intersection(dataset3_ids)

#Filter dataset3 to include only those with the common IDs.
filtered_common_dataset3 = db3[db3['ID'].isin(common_ids)]

#Calculate the overall median score for the specified columns.
overall_median_scores = filtered_common_dataset3[columns_to_check].median().mean()

#Output the overall median score.
print(f"Overall median score across all columns: {overall_median_scores:.2f}")

#Histogram displaying the data.
plt.figure(figsize=(15, 10))
for i, col in enumerate(columns_to_check):
    plt.subplot(4, 4, i + 1)
    plt.hist(filtered_common_dataset3[col].dropna(), bins=20, edgecolor='k', alpha=0.7)
    plt.title(col)
    plt.xlabel('Score')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()