#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[73]:


count=0
step=0
for i in range (1,11):
    num =np.random.randint(1,7)
    if (num<=3):
        count += 1
        if (step ==0):
            print("O level")
        else:
            step -=1    
    elif (num<=5):
        count += 1
        step +=1        
    elif (num==6):
        count += 1
        num =np.random.randint(1,7)
        print("Num: ",num)
        step = step+num

print("count: ",count)
print("Step: ",step)


# In[ ]:




