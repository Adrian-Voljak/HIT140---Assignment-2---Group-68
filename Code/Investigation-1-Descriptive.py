#Load packages that will potentially be used.
import numpy as np
import math
import scipy
import statsmodels
import pandas as pd
import matplotlib.pyplot as plt

#Load datasets.
db1 = pd.read_csv('C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT140/HIT140 Assignment 2/Code/dataset1.csv')
db2 = pd.read_csv('C:/Users/User/OneDrive/Desktop/University/Semester 2 2024/HIT140/HIT140 Assignment 2/Code/dataset2.csv')

#Checks if users are 'deprived' or not and creates two different lists to store this information.
if 'deprived' in db1.columns and 'ID' in db1.columns:
    ids_deprived = db1[db1['deprived'] == 1]['ID'].tolist()
    ids_not_deprived = db1[db1['deprived'] != 1]['ID'].tolist()

    #Find shared IDs between db1 and db2.
    if 'ID' in db2.columns:
        shared_ids_deprived = set(ids_deprived) & set(db2['ID'])
        shared_ids_not_deprived = set(ids_not_deprived) & set(db2['ID'])
        
        #Calculates averages of TV time and Video game time for deprived users.
        if shared_ids_deprived:
            filtered_db2_deprived = db2[db2['ID'].isin(shared_ids_deprived)]
            
            if 'G_we' in db2.columns and 'G_wk' in db2.columns:
                weekday_games_deprived = filtered_db2_deprived['G_we'].mean()
                weekend_games_deprived = filtered_db2_deprived['G_wk'].mean()
                overall_games_deprived = (filtered_db2_deprived['G_we'] + filtered_db2_deprived['G_wk']).mean()
                
                print(f"Deprived users:")
                print(f"  On average, users played {weekday_games_deprived:.2f} hours of video games during the week.")
                print(f"  On average, users played {weekend_games_deprived:.2f} hours of video games on the weekend.")
                print(f"  On average, users played {overall_games_deprived:.2f} hours of video games overall.")
            
            if 'T_we' in db2.columns and 'T_wk' in db2.columns:
                weekday_tv_deprived = filtered_db2_deprived['T_we'].mean()
                weekend_tv_deprived = filtered_db2_deprived['T_wk'].mean()
                overall_tv_deprived = (filtered_db2_deprived['T_we'] + filtered_db2_deprived['T_wk']).mean()
                
                print(f"  On average, users watched {weekday_tv_deprived:.2f} hours of TV during the week.")
                print(f"  On average, users watched {weekend_tv_deprived:.2f} hours of TV on the weekend.")
                print(f"  On average, users watched {overall_tv_deprived:.2f} hours of TV overall.")
        
        #Calculates averages for non-deprived users.
        if shared_ids_not_deprived:
            filtered_db2_not_deprived = db2[db2['ID'].isin(shared_ids_not_deprived)]
            
            if 'G_we' in db2.columns and 'G_wk' in db2.columns:
                weekday_games_not_deprived = filtered_db2_not_deprived['G_we'].mean()
                weekend_games_not_deprived = filtered_db2_not_deprived['G_wk'].mean()
                overall_games_not_deprived = (filtered_db2_not_deprived['G_we'] + filtered_db2_not_deprived['G_wk']).mean()
                
                print(f"Non deprived users:")
                print(f"  On average, users played {weekday_games_not_deprived:.2f} hours of video games during the week.")
                print(f"  On average, users played {weekend_games_not_deprived:.2f} hours of video games on the weekend.")
                print(f"  On average, users played {overall_games_not_deprived:.2f} hours of video games overall.")
            
            if 'T_we' in db2.columns and 'T_wk' in db2.columns:
                weekday_tv_not_deprived = filtered_db2_not_deprived['T_we'].mean()
                weekend_tv_not_deprived = filtered_db2_not_deprived['T_wk'].mean()
                overall_tv_not_deprived = (filtered_db2_not_deprived['T_we'] + filtered_db2_not_deprived['T_wk']).mean()
                
                print(f"  On average, users watched {weekday_tv_not_deprived:.2f} hours of TV during the week.")
                print(f"  On average, users watched {weekend_tv_not_deprived:.2f} hours of TV on the weekend.")
                print(f"  On average, users watched {overall_tv_not_deprived:.2f} hours of TV overall.")

            #Histogram for deprived users.
            plt.figure(figsize=(12, 6))
            plt.subplot(2, 2, 1)
            plt.hist(filtered_db2_deprived['G_we'], bins=10, alpha=0.7)
            plt.title('Weekday Video Game Time (Deprived)')
            plt.xlabel('Hours')
            plt.ylabel('Frequency')
            
            plt.subplot(2, 2, 2)
            plt.hist(filtered_db2_deprived['G_wk'], bins=10, alpha=0.7)
            plt.title('Weekend Video Game Time (Deprived)')
            plt.xlabel('Hours')
            plt.ylabel('Frequency')
            
            plt.subplot(2, 2, 3)
            plt.hist(filtered_db2_deprived['T_we'], bins=10, alpha=0.7)
            plt.title('Weekday TV Time (Deprived)')
            plt.xlabel('Hours')
            plt.ylabel('Frequency')
            
            plt.subplot(2, 2, 4)
            plt.hist(filtered_db2_deprived['T_wk'], bins=10, alpha=0.7)
            plt.title('Weekend TV Time (Deprived)')
            plt.xlabel('Hours')
            plt.ylabel('Frequency')
            
            plt.tight_layout()
            plt.show()

            #Histogram for non-deprived Users.
            plt.figure(figsize=(12, 6))
            plt.subplot(2, 2, 1)
            plt.hist(filtered_db2_not_deprived['G_we'], bins=10, alpha=0.7)
            plt.title('Weekday Video Game Time (Non-Deprived)')
            plt.xlabel('Hours')
            plt.ylabel('Frequency')
            
            plt.subplot(2, 2, 2)
            plt.hist(filtered_db2_not_deprived['G_wk'], bins=10, alpha=0.7)
            plt.title('Weekend Video Game Time (Non-Deprived)')
            plt.xlabel('Hours')
            plt.ylabel('Frequency')
            
            plt.subplot(2, 2, 3)
            plt.hist(filtered_db2_not_deprived['T_we'], bins=10, alpha=0.7)
            plt.title('Weekday TV Time (Non-Deprived)')
            plt.xlabel('Hours')
            plt.ylabel('Frequency')
            
            plt.subplot(2, 2, 4)
            plt.hist(filtered_db2_not_deprived['T_wk'], bins=10, alpha=0.7)
            plt.title('Weekend TV Time (Non-Deprived)')
            plt.xlabel('Hours')
            plt.ylabel('Frequency')
            
            plt.tight_layout()
            plt.show()
