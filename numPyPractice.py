#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


np.version.version


# In[10]:


arr =np.zeros(10)


# In[9]:


np.__version__ #getting version


# In[11]:


arr


# In[12]:


arr[4]=1


# In[13]:


arr


# In[14]:


arr2 =np.arange(10,50)


# In[15]:


arr2


# In[17]:


arr2[: : -1]


# In[18]:


arr3 = np.arange(0, 9)


# In[19]:


arr3


# In[20]:


arr3.size


# In[25]:


arr3.resize(3,3)


# In[26]:


arr3


# In[27]:


arr4=[1,2,0,0,4,0]


# In[34]:


for i in range(len(arr4)):  #np.nonzero(arr4)
    if arr4[i]!=0:
        print(i)


# In[35]:


np.nonzero(arr4)


# In[36]:


arr6= np.eye(3)


# In[37]:


arr6


# In[38]:


arr7= np.random.rand(3,3,3)


# In[39]:


arr7


# In[44]:


arr8= np.random.randint(3,18,5)


# In[45]:


arr8


# In[46]:


arr9= np.random.rand(10,10)


# In[47]:


arr9


# In[48]:


arr9.argmax()


# In[49]:


arr9.argmin()


# In[51]:


arr9.reshape(10*10).argmax()      #reshape used bcz it takes array as list


# In[53]:


arr9.reshape(10*10)[21]          #(10*10) convert it in list


# In[54]:


arr10= np.random.rand(30)


# In[55]:


arr10


# In[56]:


np.mean(arr10)                #Mean using function
    


# In[57]:


sum=0                          #Mean using for loop
for i in range (len(arr10)):
    sum +=arr10[i]
print(sum/len(arr10))    


# In[83]:


arr = np.zeros([10,10])
arr[[0,-1]]=1
arr[:,[0,-1]]=1


# In[84]:


arr


# In[86]:


arr1 = np.zeros([12,12])
arr1[1:11,1:11]=arr
arr1


# In[75]:


arr


# In[78]:


arr12=[2,4,5,1,4,2,5,6,7]


# In[3]:


arr12= np.array[3,3]


# In[ ]:




