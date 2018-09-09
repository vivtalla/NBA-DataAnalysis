
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")


# In[32]:


df = pd.read_csv('nba_elo.csv')


# In[33]:


df.head()


# In[34]:


df.tail()


# In[37]:


df.drop(df.index[:42612], inplace=True)
df


# In[38]:


df.head()


# In[61]:


df.dtypes


# In[67]:


df['season'] = pd.to_numeric(df['season']).astype(float)


# In[68]:


df.dtypes


# In[69]:


df


# In[50]:


df2 = pd.read_csv('Seasons_Stats.csv')


# In[51]:


df2


# In[52]:


df2.drop(df2.index[:14469], inplace=True)


# In[53]:


df2


# In[55]:


df2.drop(df2.index[0], inplace=True)


# In[56]:


df2


# In[57]:


headers = df2.dtypes.index


# In[58]:


headers


# In[59]:


df2.drop('Unnamed: 0', axis=1)


# In[60]:


df2.dtypes


# In[70]:


horizontalStack = pd.concat([df, df2], axis=1)


# In[71]:


horizontalStack

