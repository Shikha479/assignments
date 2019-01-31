#!/usr/bin/env python
# coding: utf-8

# In[113]:


import numpy as np


# In[114]:


arrx = np.linspace(-10,10,200)


# In[115]:


arre =np.random.rand(200)


# In[116]:


m=6
c=2


# In[125]:


arry =(m*arrx)+c + arre*20


# In[126]:


import matplotlib.pyplot as plt


# In[127]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[128]:


plt.scatter(arrx,arry)


# In[141]:


m1=0
c1=0
list1=[]
for i in range(1,2000):
    y_hat =(m1*arrx)+c1    
    z = arry-y_hat
    mse= (1/200)*np.sum(np.square(z))   #mse= mean square error
    list1.append(mse)
    m1= m1+(0.01*(1/100*(np.dot(z,arrx))))
    #arrm[i]= m1
    c1= c1+(0.01*(1/100*(np.sum(z))))


# In[137]:


print(m1,c1)
y_hat =(m1*arrx)+c1  


# In[132]:


plt.scatter(arrx,arry)
plt.plot(arrx,y_hat)


# In[133]:


plt.plot(range(len(list1)),list1)


# In[ ]:




