#!/usr/bin/env python
# coding: utf-8

# # Scipy:-
# # We have the min and max temperatures in a city In India for each months of the year.
# # We would like to find a function to describe this and show it graphically, the dataset given below.
# 
# # 1. fitting it to the periodic function
# # 2. plot the fit
# # Data
# # Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
# # Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])


months = np.arange(12)
plt.plot(months, temp_max, 'ro')
plt.plot(months, temp_min, 'bo')
plt.xlabel('Month')
plt.ylabel('Min and max temperature')


# In[10]:


from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      temp_max, [20, 10, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      temp_min, [-40, 20, 0])


# In[11]:


days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()


# # Matplotlib:
# # This assignment is for visualization using matplotlib:
# 
# 
# # Charts to plot:
# 
# 

# # 1. Create a pie chart presenting the male/female proportion

# In[12]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)


# In[14]:


titanic.head()


# In[15]:


titanic['sex'].value_counts().plot.pie(figsize=(10,10),autopct= '%2f',fontsize=25)


# # 2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

# In[16]:


titanic = titanic.dropna(subset=['sex'])

mapping = {'male' : 'blue', 'female' : 'orange'}
titanic.plot.scatter(x='age', y='fare', c=titanic['sex'].map(mapping))


# In[ ]:





# In[ ]:




