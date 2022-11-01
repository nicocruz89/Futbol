# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 11:53:42 2020

@author: Nicolas Cruz
"""
#%% 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # Data visualization
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

#%% 
# The very first look at the dataset
df = pd.read_csv("C:/Users/nicoc/OneDrive/Desktop/Futbol/dataset.csv")
df.head()

#%%
# Chile NationID = 1652. Uruguay NationID = 1657
df_chile = df.loc[df['NationID'] == 1652]
df_uruguay = df.loc[df['NationID'] == 1657]
df_uruguay.info()
#%%
# Split dataframe using groupby Age
age_chile = df_chile.groupby(['Age'])
age_chile
age_uruguay = df_uruguay.groupby(['Age'])
age_uruguay
#%%
# Let's make our first data visualization! 
f, axarr = plt.subplots(4, sharex=False, figsize=(8,10))
plt.xlim(xmax=42,xmin=18)
plt.xticks()
international_max_chile = age_chile['IntGoals'].max()
axarr[0].plot(international_max_chile, color = 'tab:red')
axarr[0].set_title('Goles internacionales máximos por grupo de edad')

international_max_uruguay = age_uruguay['IntGoals'].max()
axarr[0].plot(international_max_uruguay, color = 'tab:cyan')
axarr[0].legend(['Chile','Uruguay'])

international_max_chile = age_chile['IntCaps'].max()
axarr[1].plot(international_max_chile, color = 'tab:red')
axarr[1].set_title('Participaciones internacionales máximos por grupo de edad')

international_max_uruguay = age_uruguay['IntCaps'].max()
axarr[1].plot(international_max_uruguay,  color = 'tab:cyan')
axarr[1].legend(['Chile', 'Uruguay'])

international_sum_chile = age_chile['IntCaps'].sum()
axarr[2].plot(international_sum_chile, color = 'tab:red')
axarr[2].set_title('Participaciones internacionales totales por grupo de edad')


international_sum_uruguay = age_uruguay['IntCaps'].sum()
axarr[2].plot(international_sum_uruguay,  color = 'tab:cyan')
axarr[2].legend(['Chile','Uruguay'])


international_sum_chile = age_chile['IntGoals'].sum()
axarr[3].plot(international_sum_chile, color = 'tab:red')
axarr[3].set_title('Goles internacionales totales por grupo de edad')
axarr[3].legend(['Chile','Uruguay'])


international_sum_uruguay = age_uruguay['IntGoals'].sum()
axarr[3].plot(international_sum_uruguay,  color = 'tab:cyan')
axarr[3].set_xlabel("Age")
axarr[3].legend(['Chile','Uruguay'])


plt.tight_layout()
plt.savefig('Goles y participaciones internacionales.png', dpi = 300)

#%%
# Extracting just the physicals attributes
physicals_chile = age_chile[['Height', 'Weight', 'Acceleration', 'Pace', 'Agility', 
                 'Balance', 'Jumping', 'NaturalFitness', 'Stamina', 'Strength']]
physicals_uruguay = age_uruguay[['Height', 'Weight', 'Acceleration', 'Pace', 'Agility', 
                 'Balance', 'Jumping', 'NaturalFitness', 'Stamina', 'Strength']]
# The count for players aged 47+ is too low to feel secure about the mean so let's ignore those ages
physicals_subset_chile = physicals_chile.agg(['mean']).loc[14:46]
physicals_subset_uruguay = physicals_uruguay.agg(['mean']).loc[14:46]
#Setting up the subplot
f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10)) = plt.subplots(5, 2, figsize=(15, 20))

ax1.plot(physicals_subset_chile['Height'], color = 'tab:red')
ax1.set_title('Height')

ax1.plot(physicals_subset_uruguay['Height'], color = 'tab:cyan')
ax1.set_title('Height')

ax2.plot(physicals_subset_chile['Weight'], color = 'tab:red')
ax2.set_title('Weight')

ax2.plot(physicals_subset_uruguay['Weight'], color = 'tab:cyan')
ax2.set_title('Weight')

ax3.plot(physicals_subset_chile['Acceleration'], color = 'tab:red')
ax3.set_title('Acceleration')

ax3.plot(physicals_subset_uruguay['Acceleration'], color = 'tab:cyan')
ax3.set_title('Acceleration')

ax4.plot(physicals_subset_chile['Pace'], color = 'tab:red')
ax4.set_title('Pace')

ax4.plot(physicals_subset_uruguay['Pace'], color = 'tab:cyan')
ax4.set_title('Pace')

ax5.plot(physicals_subset_chile['Agility'], color = 'tab:red')
ax5.set_title('Agility')

ax5.plot(physicals_subset_uruguay['Agility'], color = 'tab:cyan')
ax5.set_title('Agility')

ax6.plot(physicals_subset_chile['Balance'], color = 'tab:red')
ax6.set_title('Balance')

ax6.plot(physicals_subset_uruguay['Balance'], color = 'tab:cyan')
ax6.set_title('Balance')

ax7.plot(physicals_subset_chile['Jumping'], color = 'tab:red')
ax7.set_title('Jumping')

ax7.plot(physicals_subset_uruguay['Jumping'], color = 'tab:cyan')
ax7.set_title('Jumping')

ax8.plot(physicals_subset_chile['NaturalFitness'], color = 'tab:red')
ax8.set_title('NaturalFitness')

ax8.plot(physicals_subset_uruguay['NaturalFitness'], color = 'tab:cyan')
ax8.set_title('NaturalFitness')

ax9.plot(physicals_subset_chile['Stamina'], color = 'tab:red')
ax9.set_title('Stamina')

ax9.plot(physicals_subset_uruguay['Stamina'], color = 'tab:cyan')
ax9.set_title('Stamina')

ax10.plot(physicals_subset_chile['Strength'], color = 'tab:red')
ax10.set_title('Strength')

ax10.plot(physicals_subset_uruguay['Strength'], color = 'tab:cyan')
ax10.set_title('Strength')

# Adding legend and title for the subplot
f.legend(['Chile', 'Uruguay'])
f.suptitle('Aspectos Fisicos por Grupos de Edad', fontsize=16)
plt.tight_layout()
plt.savefig('Aspectos fisicos por grupos de edad.png', dpi = 300)
