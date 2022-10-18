# -*- coding: utf-8 -*-

"""

@author: Chase_Yi

"""

#%%
import pandas as pd

data = pd.read_csv("C:/Users/47804/Desktop/desktop/DSTI/Clean IT/colab_exercise_data.csv")

data.head(10)

#%%
import matplotlib.pyplot as plt

import seaborn as sns

print(data.head())

print(data.tail())

print(data.shape)

print(data.info())

#%%

# draw scatter plot
plt.scatter(x=data['Profit'], y=data['Cost'])

#%%

# draw pie chart
data['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))

#%%

# draw bar plot
ax = data['Country'].value_counts().plot(kind='bar', figsize=(14,6))

#%%

# draw histogram
sns.displot(data['Revenue'], kind="kde")

# In statistics, kernel density estimation (KDE) is a non-parametric way 
# to estimate the probability density function (PDF) of a random variable. 
# This function uses Gaussian kernels and includes automatic bandwidth determination.

#%%

# show correlation matrix
corr = data._get_numeric_data().corr()

corr

#%%

# show heat map
fig = plt.figure(figsize=(8,8), dpi=400) 

sns.heatmap(corr,cmap='RdBu',annot=True)

#%%

# show density plot
ax = data['Unit_Cost'].plot(kind='density', figsize=(14,6))
ax.axvline(data['Unit_Cost'].mean(), color='red')
ax.axvline(data['Unit_Cost'].median(), color='green')

#%%

# show pair plots
sns.pairplot(data.iloc[:, 12:15],kind="reg",diag_kind="kde")

