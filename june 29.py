#!/usr/bin/env python
# coding: utf-8

# In[3]:


##create a series by passing a list of values
import pandas as pd
a=pd.Series([1,3,4,5,6,7])
print(a)


# In[4]:


##missing values then it can be nan of numpy
import numpy as np
a=pd.Series([1,2,3,4,np.nan,6])
print(a)


# In[8]:


## create a list of data with in particular range
import pandas as pd
dates=pd.date_range('20190601',periods=20)
print(dates)


# In[ ]:


##creating a dict converted into series of values
a=pd.DataFrame({'A':1.,
                'B':pd.Timestamp("20190601"),
                'C':pd.Series(1,index=list(range(4)),dtype='float32'
                'D':np.array([3]*4,dtype='int32')                             


# In[9]:


## drawing a square
import turtle as tt
a1=tt.Turtle()
a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)


a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

tt.done()


# In[ ]:




