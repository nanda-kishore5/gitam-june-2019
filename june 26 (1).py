#!/usr/bin/env python
# coding: utf-8

# In[2]:


##STRING FUNCTIONS-IN BUILT FUNCTIONS
##UPPER()-RETURNS STRINGS WHICH ALL THE CHARACTERS IN UPPER CASE
str="pyHton"
print(str.upper())
print(str.lower())


# In[14]:


##BOOLEAN METHODS
##WHETHER THE GIVEN CHARACTER IS UPPER OR NOT islower()
##IF IT IS UPPER IT RETURNS TRUE OTHERWISE IT RETURNS FALSE isupper()
##isnumeric()
##isalpha() it returns true if it has all alphabets 
s="Python is easy Programmimg to learn"
s1="Python"
s2=" fgf gjj hkjk"
print(s.islower())
print(s1.islower())
print(s1.isupper())
print(s2.isnumeric())
print(s1.isalpha())
print(s1.istitle())
print(s2.isspace())


# In[31]:


###STRING METHODS
##1.join()
##2.split()
##3.replace()

str="python"
print("*".join(str))


# In[32]:


str="p*y*t*h*o*n"
print(str.replace("*",""))


# In[17]:


print(",".join(["join","python"]))


# In[24]:


##SPLIT FUNCTION
s="python programming is easy to learn"
print(s.split())
print(s.split("a"))
lst=s.split()
print(lst.index("is"))


# In[25]:


s="python programming is easy to learn"
lst= list(s)
print(lst)


# In[26]:


##REPLACE()
s="python programming is easy to learn"
print(s.replace("gra","application"))


# In[28]:


hello=0
print(3,hello)


# In[35]:


##TUPLES IN PYTHON
t1=("python","programming",1989,2019,"machine learning","ai")
t2=(1,2,3,4,5)
print(t1)
print(t2)


# In[41]:


t1=("python","programming",1989,2019,"machine learning","ai")
print("t1[0]=",t1[0])
print("t1[4]=",t1[4])
print("t1[-1]=",t1[-1])
print("t1[1:4]=",t1[1:4])
print("t1[2:-2]=",t1[2:-2])


# In[46]:


t1=("python","programming",1989,2019,"machine learning","ai")
print(t1)
del t1
print(t1)


# In[47]:


t1=("python","programming")
t2=(1989,2019,"ml","ai")
t3=t1+t2
print(t3)


# In[ ]:


##TUPLE METHODS
##1.len(tuple)
##2.max(tuple)
##3.min(tuple)
##cmp(tuple1,tuple2)


# In[50]:


t1=(1,2,3,5,6,7)
print(max(t1))
print(min(t1))
print(len(t1))


# In[51]:


t1=(1,2,3,4,5)
t2=(1,2,3,4,5)
print(t1)
print(t2)


# In[53]:


list1=["python","programming",1989,2019,"machine learning","ai"]
print(list1)
tuple1=tuple(list1)
print(tuple1)


# In[62]:


###PYTHON-DICTIONARY
user1={'name':'python','age':29,'emailid':'gmail.com','mobileno':888888888888}
print("user1[name]=",user1["name"])
print("user1[age]=",user1["age"])
print("user1[emailid]=",user1["emailid"])
print("user1[mobileno]=",user1["mobileno"])


# In[65]:


##updation of dictionary data
user1={'name':'python','age':29,'emailid':'gmail.com','mobileno':888888888888}
print(user1["emailid"])
user1["emailid"]="Gmail.com"
print(user1["emailid"])
user1["address"]="hyderabad"
print(user1["address"])


# In[71]:


user1={'name':'python','age':29,'emailid':'gmail.com','mobileno':888888888888}


del user1["emailid"]

user1.clear()
del user1


# In[76]:


##METHODS IN DICTIONARY
##1.len(dicobj)
##2.str(dicobj)
##3.copy(dicobj)
##4.items()
user1={'name':'python','age':29,'emailid':'gmail.com','mobileno':888888888888}
print(user1)
user1["address"]="hyd"
print(len(user1))


# In[75]:


user1={'name':'python','age':29,'emailid':'gmail.com','mobileno':888888888888}
print(str(user1))


# In[80]:


user1={'name':'python','age':29,'emailid':'gmail.com','mobileno':888888888888}
user2=user1.copy()
print(user1)
print(user2)
user1["address"]="hyd"
print(user1)
print(user2)


# In[82]:


user1={'name':'python','age':29,'emailid':'gmail.com','mobileno':888888888888}
print(user1.items())


# In[87]:


user1={'name':'python','age':29,'emailid':'gmail.com','mobileno':888888888888}
user2=user1.copy()
print(user1.values())
print(user2.values())


# In[94]:


###STRING FOMATTING
##%s %d
lst=["python","programming"]
print("%s %s"%(lst[0],lst[1]) )


# In[103]:


lst=["python","programming"]
print("{0} {1}".format(lst[0],lst[1]))


# In[122]:


lst=[1,2,3,4]
print("%d %d %d %d"%(lst[0],lst[1],lst[2],lst[3]))


# In[123]:


lst=[1,2,3,4]
print("value at :{0} value at {1}".format(lst{0},lst{1})


# In[96]:


print('1.1'.isnumeric())


# In[97]:


print('abcdefcdghcd'.split('cd', 2))


# In[98]:


print('Hello!2@#World'.istitle())


# In[107]:


##CONTACT APPLICATION
##WHETHER THE GIVEN ELEMENTS PRESENT IN DICTIONARY OR NOT
##ADDING A CONTACT
contacts={}
def addcontact(name,phone):
    if name not in contacts:
        contacts[name]=phone
        print("contact %s added"% name)
    else:
        print("contact %s already exists"% name)
        return
addcontact("anil",99999999999)
addcontact("vinil",8888888888)
addcontact("anil",999887879999)


# In[110]:


#SEARCH FOR A PARTICULAR CONTACT FROM CONTACT LIST
def searchcontact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("%s does not exists"% name)
    return
searchcontact("anil")
searchcontact("baby")


# In[115]:


##NEW CONTACTS GIVEN AS A DICTIONARY
##MERGE NEW CONTACTS WITH EXISTING CONTACTS

def importcontacts(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added successfully")
    return
newcontacts={"sai":878456454}
importcontacts(newcontacts)


# In[116]:


##DELETE A CONTACT FROM CONATCT LIST
def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name,": is deleted from contacts")
    else:
        print(name,"; is not exists in the contacts")
    return
deletecontact("anil")


# In[117]:


print(contacts)


# In[120]:


##MODIFYING A CONTACT
def updatecontact(name,phone):
    if name in contacts:
        contacts[name]=phone
        print(name,": updated with new phone no")
    else:
        print(name,": not exists in contacts")
    return
updatecontact("sai",65464645454)
updatecontact("anil",6546544874)
        


# In[124]:


##PACKAGES AND MODULES
from math import floor as f1
f1(123.999)


# In[125]:


from math import factorial as fact
fact(5)


# In[126]:


#generate the random no between two limits
import random
def generaterandoms(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
generaterandoms(10,12,120) 


# In[ ]:




