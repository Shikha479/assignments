#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
nums=random.randint(1000,9999)
num=str(nums)
nk1=input()
m=len(nk1)
lm=[mn for mn in num]
ln=[nm for nm in nk1]
cw=[0,0]
print(nums)
while(cw[0]!=4):
    for i in range(m):
        if lm[i]==ln[i]:
            cw[0]=+1
        elif(lm[i] in ln[i]):
            cw[1]=+1
    nk1=input()        
    m=len(nk1) 
    ln=[nm for nm in nk1]
print(cw[0])
print(cw[1])


# In[ ]:





# In[ ]:




