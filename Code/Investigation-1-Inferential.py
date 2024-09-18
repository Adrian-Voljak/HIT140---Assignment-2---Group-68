#Load packages that will potentially be used.
import numpy as np
import math
import scipy
from scipy.stats import pearsonr
import statsmodels
import pandas as pd
import matplotlib.pyplot as plt

#Load datasets.
db2 = pd.read_csv('C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT140/HIT140 Assignment 2/Code/dataset2.csv')
db3 = pd.read_csv('C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT140/HIT140 Assignment 2/Code/dataset3.csv')

#Identify IDs with the highest amount of hours spent watching TV from both the weekday and weekend, then combine them into a new column named T_hours. Furthermore, sort them so the highest values are at the top.
db2['T_hours'] = db2[['T_we', 'T_wk']].max(axis=1)
max_tv_hours_ids = db2[['ID', 'T_hours']].sort_values(by='T_hours', ascending=False)['ID']

# Filter and merge the datasets to get the IDs that have both the highest hours and the correlating Usef score.
filtered_dataset3 = db3[db3['ID'].isin(max_tv_hours_ids)]

merged_data = pd.merge(db2[['ID', 'T_hours']], filtered_dataset3[['ID', 'Usef']], on='ID')

#Calculate the correlation between T_hours and Usef.
correlation, p_value = pearsonr(merged_data['T_hours'], merged_data['Usef'])

#Output the results and interpret the hypothesis to either reject or accept it.
print(f"Correlation between highest hours spent watching TV and feeling useful: {correlation:.2f}")
print(f"P-value of the correlation test: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant correlation between TV hours and feeling useful.")
else:
    print("Failed to reject the null hypothesis: There is no significant correlation between TV hours and feeling useful.")

#Scatterplot to display data.
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['T_hours'], merged_data['Usef'], color='blue', edgecolor='k', s=50)
m, b = np.polyfit(merged_data['T_hours'], merged_data['Usef'], 1)
plt.plot(merged_data['T_hours'], m * merged_data['T_hours'] + b, color='red')
plt.title('Scatter Plot of TV Hours vs. Feeling Useful')
plt.xlabel('Hours Spent Watching TV')
plt.ylabel('Feeling Useful Score')
plt.grid(True)
plt.show()