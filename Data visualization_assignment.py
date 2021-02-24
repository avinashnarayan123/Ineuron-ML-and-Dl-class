#!/usr/bin/env python
# coding: utf-8

# # In this assignment students have to transform iris data into 3 dimensions
# # and plot a 3d chart with transformed dimensions and colour each data
# # point with specific class.

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets


# In[6]:


import seaborn as sns
iris = sns.load_dataset('iris')


# In[7]:


iris.head()


# In[10]:


ax= plt.axes(projection= '3d')
ax.scatter3D(iris['sepal_length'], iris['sepal_width'],iris['petal_length'])


# In[ ]:




