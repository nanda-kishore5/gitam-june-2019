#!/usr/bin/env python
# coding: utf-8

# ## OBJECTED ORIENTED PROGRAMMING
# 

# In[10]:


def test():
    print("test() for function")
    return
test()


# In[6]:


class demo:
    def test(self):
        print("test() for the class and method")
        return
obj=demo()
obj.test()


# In[19]:


class demo1:
    def fact(self,n):
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
        return fact
p1=demo1()
p1.fact(5)


# In[20]:


class demo2:

    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def add(self,p1,p2):
        return p1+p2
c1=demo2(10,20)
print(c1.add(100,200))


# In[30]:


## some inheritance
class person(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemployee(self):
        return False
    
## derived class
class employee(person):
    def isemployee(self):
        return True
emp=person("anil")
print(emp.getname(),emp.isemployee())

emp1=employee("akhil")
print(emp1.getname(),emp1.isemployee())


# In[37]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
print(array)


# In[39]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
print(array.shape)
print(array.dtype)


# In[43]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1.shape)
a2=np.array([(1,2),(3,4),(5,6)])
print(a2.shape)


# In[44]:


## re shape the given array
a1=np.array([(1,2,3),(4,5,6)])
print(a1)
a1.reshape(3,2)


# In[49]:


##append some data---horizontally

a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.hstack((a1,a2)))


# In[51]:


##append some data---vertically

a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.vstack((a1,a2)))


# In[52]:


##generte random no from np
a1=np.random.normal(5,0.5,10)
print(a1)


# In[53]:


np.zeros((2,2))


# In[55]:


np.ones((4,3),dtype=np.int64)


# In[57]:


a=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(a)[2]=5
print(a)


# In[62]:


import numpy as np
np.arange(1,10)
np.arange(1,100,9)


# In[64]:


np.arange(2,20,2)
np.arange(1,25,2)


# In[68]:


a1=np.array([(1,2,3),(4,5,6)])
print("first row :",a1[0])


# In[65]:


a1=np.array([(1,2,3),(4,5,6)])
print("second row :",a1[1])


# In[66]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing column :",a1[:,1])


# In[69]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing last column :",a1[:,2])


# In[71]:


a1=np.random.normal(5,1,20)
print(a1)
print("min value= ",np.min(a1))
print("max value= ",np.max(a1))
print("mean value= ",np.mean(a1))
print("median value= ",np.median(a1))


# In[72]:


c1=np.array([(1,2),(3,4)])
c2=np.array([(3,4),(1,2)])
np.dot(c1,c2)


# In[73]:


c1=np.array([(1,2),(3,4)])
c2=np.array([(3,4),(1,2)])
np.matmul(c1,c2)


# In[86]:


import pandas as pd
dict={"name":["anil","akhil","dinesh"],"emailid":["anil@gmail.com","akhil@gmail.com","dinesh@gmail.com"],"mobile no":[999,888,777],"address":["hyd","hyd","hyd"]}
b=pd.DataFrame(dict)
print(b)


# In[ ]:




