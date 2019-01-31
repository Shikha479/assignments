#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[9]:


outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[10]:


outside


# In[11]:


inside


# In[12]:


hier_index


# In[13]:


list(zip(outside,inside))


# In[14]:


df = pd.DataFrame(np.random.randn(6,2), hier_index,['A','B'])
df


# In[16]:


df.loc['G1'].loc[1]


# In[18]:


df.index.names = ['Groups', 'Num']             


# In[19]:


df


# In[22]:


df.loc['G2'].loc[2].loc['B']


# In[24]:


df.loc['G2'].loc[2]['A']


# In[25]:


df.xs


# In[26]:


df.xs('G1')                #cross-section


# In[27]:


df.loc['G2']


# In[28]:


df.xs('G2')


# In[32]:


df.xs(1,level='Num')


# In[30]:





# In[ ]:




