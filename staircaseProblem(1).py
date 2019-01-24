#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[25]:


count=0
step=0
for i in range (1,11):
    num =np.random.randint(1,7)
    if (num<=3):
        count += 1
        if (step !=0):
            step -=1         
    elif (num<=5):
        count += 1
        step +=1        
    elif (num==6):
        count += 1
        num1 =np.random.randint(1,7)
        #print("Num: ",num)
        step = step+num1

print("count: ",count)
print("Step: ",step)


# In[21]:


count=0
#step=0
list1=[]
dice=[1,2,3,4,5,6]
for i in range(1,100):
    step=0
    for i in range(1,100):
        num =np.random.choice(dice, p=[.25,0.25,0.25,1/12,1/12,1/12])
        if (num<=3):
            #count += 1
            if (step !=0):
                step-=1   
        if (num<=5):
            #count += 1
            step +=1        
        if (num==6):
            #count += 1
            num1 =np.random.choice(dice, p=[.25,0.25,0.25,1/12,1/12,1/12])
            #print("Num: ",num)
            step = step+num1
    list1.append(step)          

print("count: ",count)
print("Step: ",list1)


# In[ ]:





# In[ ]:




