#!/usr/bin/env python
# coding: utf-8

# In[2]:


##FILE HANDLING IN PYTHON
##FUNCTION TO CREATE A FILE AND WRITE SOME DATA

def createfile(filename):
    f=open(filename,"w")
    for i in range(10):
        f.write("this is %d line\n" % i)
    print("file is created successfully and data has been written")
    f.close()
    return
createfile("file1.txt")


# In[49]:


##function for reading a file

def readfile(filename):
    f=open(filename,"r")
    if f.mode=="r":

        x=f.read()
        print(x)
    f.close()
    return
readfile("file1.txt")


# In[4]:


##data to append
##function to append the data to existing file

def appenddata(filename):
    f=open(filename,"a")
    f.write("newline 1\n")
    f.write("new line")
    return
appenddata("file1.txt")


# In[7]:


def dataanalysiswordcount(filename,word):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split()
    count=lst.count(word)
    return count
print(dataanalysiswordcount("file1.txt","rest"))


# In[45]:


##function to count of characters in the file
def countofcharacters(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    return len(lst)
print(countofcharacters("file1.txt"))


# In[37]:


##function to count upper case characters
def uppercase(filename):
    count=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.islower():
            count=count+1
    return count
print(uppercase("file1.txt"))


# In[48]:


##function to count nof lines
def nooflines(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split('\n')     
    return len(lst)
print(nooflines("file1.txt"))


# In[57]:


##regular expression for indian mobile no
##validation for emailid
##username@omainname.extension

import re 
def phonenovalidate(phone):
    pattern ='^[6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenovalidate(9553955670))
print(phonenovalidate(95539570))
        


# In[62]:


##first digit 0 case
import re 
def phonenovalidate(phone):
    pattern ='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenovalidate("09553955670"))
print(phonenovalidate("+919553955670"))


# In[72]:


##validate roll no
##152U1A0501

def validaterollno(number):
    number=str(number)
    pattern='^[1][5][2][U][1][A][0][1-9][0-6][0-9]$'
    if re.match(pattern,number):
        return True
    return False
print(validaterollno("152U1A0485"))
print(validaterollno("152U1A0501"))


# In[71]:


##040-456258
def validatelandno(number):
    number=str(number)
    pattern='^[0][4][0][-][0-9]{8}$'
    if re.match(pattern,number):
        return True
    return False
print(validatelandno("040-40117502"))


# ### validate vehicle no for TS
# * TS 10 EE 5386   ... [True]

# In[87]:


def validatevehicleno(number):
    number=str(number)
    pattern='^[T][S][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9][0-9]$'
    if re.match(pattern,number):
        return True
    return False
print(validatevehicleno("TS21EE5386"))
print(validatelvehicleno("AP21EE5386"))


# In[95]:


import re
def validateemailid(email):
    number=str(email)
    pattern='^[0-9a-z][0-9a-z .]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
            return True
    return False
print(validateemailid("anil1234@gmail.com"))


# In[ ]:


import re
def validatepassword(s):
    pattern='^[a-zA-Z]'

