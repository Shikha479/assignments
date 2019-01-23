#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np


# In[63]:


arr =np.arange(0,12)


# In[64]:


arr.shape


# In[56]:


arr =np.array


# In[4]:


np.arange(1,11,3)


# In[5]:


np.zeros(10)


# In[65]:


arr.reshape(6,2)


# In[14]:


np.eye(4)*5


# In[ ]:


arr2= np.arange(0.12) 


# In[17]:


arrtemp= np.array([1,2,3,5])


# In[18]:


arrtemp += 1


# In[19]:


arrtemp


# In[21]:


arrtemp.dtype


# In[22]:


import datetime as dt


# In[23]:


dt.datetime.now()


# In[79]:


arr2 =np.random.rand(2,1000)


# In[80]:


arr2.shape


# In[81]:


arr2


# In[77]:


arr2[0][3]


# In[89]:


t1= dt.datetime.now()
dotprod =np.dot(arr2[0,:],arr2[1,:])
t2 =dt.datetime.now()
print(t2-t1,dotprod)


# In[90]:


arr2.shape


# In[92]:


t1= dt.datetime.now()
sum1=0
for i in range(arr2.shape[1]):
    sum1+= arr2[0][i]*arr2[1][i]
t2 =dt.datetime.now()
print(t2-t1,sum1)                  
                    
                    


# In[55]:


arr


# In[93]:


arr3 = np.arange(2,23)


# In[94]:


arr3


# In[95]:


np.sin(arr2)


# In[97]:


arr3= [12,23,12,34,4,6,7,4,2,6,8,5]


# In[102]:


arr4 =np.random.rand(2,10,4)


# In[105]:


arr4


# In[114]:


arr4.reshape(2*10*4).argmax()


# In[115]:


arr4.reshape(2*10*4)[19]


# In[113]:


arr4.shape


# In[116]:


arr5 = np.random.rand(2,10,4)


# In[117]:


arr5


# In[118]:


arr4 + arr5


# In[119]:


arr5(2,9,3)


# In[ ]:




