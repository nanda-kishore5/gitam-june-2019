#!/usr/bin/env python
# coding: utf-8

# In[4]:


def printeven(n):
    count=0
    sum=0
    while(count!=n):
        if(count%2==0):
            sum=sum+count
        count=count+1
    return sum
        
print(printeven(20))    


# In[ ]:


##functional programming
##factors of a given number


# In[5]:


def factorslist(n):
    i=1
    while(i!=n):
        if(n%i==0):
            print(i,end= " ")
        i=i+1
    return
factorslist(12)


# In[ ]:


##list in python
##examples of lists


# In[6]:


list1=[1,2,3,4,5];
print(list1)
#list[0]
print(list1[0])


# In[8]:


list2=["sai","uma"];
for x in list2:
    print(x,end=" ")


# In[16]:


##list example with particular index
list1=[1,2,3,4,5,6,7];
for x in list1:
    print(x,end="  ")
print()
print(list1[4])
print(list1[3:7])
print(list1[0:3])


# In[25]:


list1=[1,2,3,4,5,6,7,8,9,10];
for x in list1:
    print(x,end=" ")
print()
print(list1[1:-1])
print(list1[::2])
print(list1[::-2])


# In[38]:


list1=["sai",1,"akhil","gitam"];
print(list1)
list1[1]=15
print(list1)
del list1[3]
print(list1)
list2=[1,2,3,4];
print(list1+list2)
print(len(list1))
list1.append(1234)
print(list1)
print(len(list1))
print(list1.count(1234))



# In[52]:


##list with index
list1=["raptor","python","raptor","python","gitam",1]
print(list1)
list1.index("python")
list1.index(1)
list1.insert(2,2019)
print(list1)
print(len(list1))



# In[54]:


##list with remove
list1=["gitam","python","raptor",1,5,"python","python"]
print(list1)
list1.remove("python")
print(list1)
list1.remove("python")
print(list1)
list1.reverse()
print(list1)


# In[58]:


## DATA STRUCTURES
##LINEAR SEARCH
def ls(a,searchitem):
    flag=0
    for i in range(len(a)):
        if(a[i]==searchitem):
            flag=1
            break
    if(flag!=0):
        print("search element is found")
    else:
        print("element not found")
a=[1,2,4,5,6]
ls(a,33)


# In[62]:


##linear SEARCH duplicate
def lsduplicate(a,searchitem):
    flag=0
    for i in range(len(a)):
        if(a[i]==searchitem):
            flag=flag+1
    print(flag)
    
a=[1,2,3,4,5,6,6]
lsduplicate(a,6)


# In[ ]:




