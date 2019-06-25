#!/usr/bin/env python
# coding: utf-8

# In[9]:


##BINARY SEARCH
def bs(a,lindex,rindex,searchitem):
    while(lindex<=rindex):
        mindex=lindex+(rindex-rindex)//2
        if(a[mindex]==searchitem):
            return mindex
        if(a[mindex]>searchitem):
            rindex=mindex-1
        else:
            lindex=mindex+1
    return -1
list1=[1,4,9,15,25,45,57,88,98]
res=bs(list1,0,1,12)
if(res!=-1):
    print("item is found")
else:
    print("item is not found")


# In[16]:


##SORTING TECHNIQUES
##BUBBLE SORT
def sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        print(a[i],end=" ")
list1=[1,5,8,3]
sort(list1)

    


# In[17]:


##STRINGS IN PYTHON
#creating a string
str="application"
print(str)


# In[23]:


str="application"
print(str)
print("str[-1]=",str[::-1])
print("str[0]=",str[0])
print("str[1]",str[1])
print("str[:5]",str[::5])


# In[24]:


s='foo'
t='bar'
print('barf' in 2*(s+t))


# In[25]:


s[:]==s


# In[34]:


##palindrome or not by using string
def ispalindrome(s):    
    if(s==s[::-1]):
        return True
    else:
        return False
print(ispalindrome("121"))
print(ispalindrome("nitin"))


# In[54]:


##count the digits of a number by using string
def length(n):
    return len(n)


print(length("454641646"))


# In[63]:


def count(str):
    list=list[str]
    return len(list)
count("app")

    


# In[4]:


def countuppercase(str):
    count=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=65 and ord(lst[x])<=90:
            count=count+1
    return count

print(countuppercase("Application"))
print(countuppercase("TeST"))


# In[8]:


def printdigits(str):
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            print(lst[x],end="")
print(printdigits("Application1889"))            
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




