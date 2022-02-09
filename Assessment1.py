#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import datetime
from sqlalchemy import create_engine
p_engine=create_engine("postgresql://postgres:A2580947Ar@localhost:5432/etl_project2")


# In[2]:


df1 = pd.read_csv("all_years_o3.csv")
df1.head()


# In[3]:


df2 = pd.read_csv("all_years_pm25.csv")
df2.head()


# In[4]:


df1.drop(df1.columns[[5,6,7]], axis=1, inplace=True)
df1.head()


# In[5]:


df1.columns = ['Date', 'Country', 'City','Specie', 'Count_o3']
df1.head()


# In[6]:


df1.drop(df1.columns[[3]], axis=1, inplace=True)
df1.head()


# In[7]:


df2.drop(df2.columns[[5,6,7]], axis=1, inplace=True)
df2.head()


# In[8]:


df2.columns = ['Date', 'Country', 'City','Specie', 'Count_pm25']
df2.head()


# In[9]:


df2.drop(df2.columns[[3]], axis=1, inplace=True)
df2.head()


# In[10]:


new_df = pd.merge(df1, df2,  how='left', left_on=['Date','Country', 'City'], right_on=['Date','Country', 'City'])
new_df.head()


# In[23]:


df = pd.DataFrame(new_df)
df.to_csv('Downloads/file2.csv')


# In[28]:


df7=pd.read_csv('Downloads/file2.csv',index_col=False)
df7.to_sql('file2',p_engine,if_exists='replace',index=False)


# In[24]:


z=pd.read_csv('Downloads/file2.csv')


# In[25]:


z.head()


# In[ ]:




