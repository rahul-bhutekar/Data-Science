#!/usr/bin/env python
# coding: utf-8

# # Decision Tree - Hotel Reservations

# In[1]:


# load libraries
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


# In[2]:


# read file using read_csv function
df = pd.read_csv('./Hotel_Reservations.csv')
df.head()


# ## Basic EDA

# In[3]:


# number of rows and columns
df.shape


# In[4]:


# data type of each column
df.dtypes


# In[5]:


# summary of the data: column names, total no.of non-null values, data types, memory usage
df.info()


# In[6]:


# summary statistics for numeric data types
df.describe()


# In[7]:


# summary statistics for object data types
df.describe(include=['O'])


# In[8]:


df.isna().sum()


# In[9]:


# count of duplicate rows
df[df.duplicated()].shape


# ## Decision Tree

# In[10]:


df.columns


# In[11]:


#droping the Booking ID column
df.drop(['Booking_ID'], axis=1, inplace=True)
df.head()


# In[12]:


X = df.drop('booking_status', axis=1)
y = df['booking_status']


# In[13]:


X


# In[14]:


y


# In[15]:


# Splitting the dataset into train and test
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=44)


# In[16]:


# importing 'OneHotEncoder' to convert categorical variables into numerical values
from sklearn.preprocessing import OneHotEncoder

# Create a OneHotEncoder
onehot_encoder = OneHotEncoder(drop='first', sparse=False)

# Apply the OneHotEncoder to the 'type_of_meal_plan', 'room_type_reserved', 'market_segment_type' columns
X_train_encoded = onehot_encoder.fit_transform(X_train[['type_of_meal_plan', 'room_type_reserved', 'market_segment_type']])

X_test_encoded = onehot_encoder.fit_transform(X_test[['type_of_meal_plan', 'room_type_reserved', 'market_segment_type']])


# In[17]:


X_train_encoded_df = pd.DataFrame(X_train_encoded)
X_test_encoded_df = pd.DataFrame(X_test_encoded)


# In[18]:


X_train_no_categorical = X_train.drop(['type_of_meal_plan', 'room_type_reserved', 'market_segment_type'], axis=1)
X_test_no_categorical = X_test.drop(['type_of_meal_plan', 'room_type_reserved', 'market_segment_type'], axis=1)


# In[19]:


X_train_final = pd.concat([X_train_encoded_df, X_train_no_categorical], axis=1)
X_test_final = pd.concat([X_test_encoded_df, X_test_no_categorical], axis=1)


# In[20]:


from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.fit_transform(y_test)


# In[21]:


y_train_final = pd.DataFrame(y_train_encoded)
y_test_final = pd.DataFrame(y_test_encoded)


# In[22]:


y_train_final


# In[23]:


X_train_final


# ### Building Decision Tree Classifier using Entropy as a Criterion

# In[24]:


# Convert feature names to strings
X_train_final.columns = X_train_final.columns.astype(str)


# In[25]:


print("Number of samples in X_train_final:", X_train_final.shape[0])
print("Number of samples in y_train_final:", y_train_final.shape[0])


# In[26]:


print("Missing values in X_train_final:", X_train_final.isnull().sum())
print("Missing values in y_train_final:", y_train_final.isnull().sum())


# In[27]:


# import the decisiontree classifier algorithm
from sklearn.tree import DecisionTreeClassifier

# Train the classifier on the training data
model = DecisionTreeClassifier(criterion='entropy', random_state=44)
model.fit(X_train_final, y_train_final)

