#!/usr/bin/env python
# coding: utf-8

# # EDA Assignment - Movie

# In[1]:


# load libraries
import pandas as pd
import numpy as np


# In[2]:


# read movies data
df = pd.read_csv('./dataset/Movie.csv')
df.head()


# In[3]:


df.describe()


# In[4]:


df.dtypes


# In[5]:


# summary of the data: column names, total no.of non-null values, data types, memory usage
df.info()


# In[6]:


df.shape


# ## Duplicates

# In[7]:


# count of duplicate rows
df[df.duplicated()].shape


# ##### no duplicates rows found hence, no need to use drop duplicate function

# ## Outlier detection

# ### Bar graph

# In[8]:


df['userId'].value_counts().plot.bar()


# In[9]:


df['movie'].value_counts().plot.bar()


# In[10]:


df['rating'].value_counts().plot.bar()


# ### Boxplot

# In[11]:


# import maxplotlib library
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

data = df
data_box = data.dropna()
data_box1 = data_box.userId
box1 = plt.boxplot(data_box1)


# In[12]:


data_box2 = data_box.rating
box2 = plt.boxplot(data_box2)


# In[13]:


# To get the whiskers# To get the whiskers
[item.get_ydata()[1] for item in box1['whiskers']]


# In[14]:


[item.get_ydata()[1] for item in box2['whiskers']]


# ## Missing values and Imputation

# In[15]:


import seaborn as sns

cols = data.columns
colors = ['#000099', '#ffff00'] # specify the colours - yellow is missing. blue is not missing.
sns.heatmap(data[cols].isnull(), cmap=sns.color_palette(colors))


# In[16]:


data[data.isnull().any(axis=1)].sum()


# #### We have 0 null values so we do not need Mean Imputation

# ## Scatter plot and Correlation

# In[17]:


plt.scatter(df['userId'], df['rating'])
plt.show()


# In[18]:


# Create the default pairplot
sns.pairplot(data)


# In[21]:


sns.scatterplot(data, x='userId', y='rating', hue='movie')


# ## Transformation - Dummy variabe 

# In[22]:


# generating dummy values for 'movie' column
data_cleaned = pd.get_dummies(data, columns=['movie'])
data_cleaned


# In[23]:


# correlation
data_cleaned.corr()


# # Transformations

# ## Normalization

# In[24]:


data_cleaned.info()


# In[25]:


data_cleaned.values


# ##### standarizing all movie columns

# In[26]:


# standarize the data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_cleaned.iloc[:,1:])
scaled_data


# In[27]:


from numpy import set_printoptions

set_printoptions(precision=2)
scaled_data


# # EDA with libraries

# In[28]:


# check if a Library is installed or not
get_ipython().system('pip show ydata_profiling')


# In[29]:


from ydata_profiling import ProfileReport

report = ProfileReport(df, title="Movie EDA Report")
report.to_file(output_file='eda-movies-report.html')


# In[30]:


report


# In[36]:


# check if a Library is installed or not
get_ipython().system('pip show sweetviz')


# In[37]:


import sweetviz as sv

sweet_report = sv.analyze(df)
sweet_report.show_html('eda-movies-sweetviz-report.html')


# In[38]:


# to display the sweetviz report in the notebook
sweet_report.show_notebook(  w='100%', 
                             h=530, 
                             scale=None,
                             layout='widescreen',
                             filepath='./eda-movies-sweetviz-report.html' )

