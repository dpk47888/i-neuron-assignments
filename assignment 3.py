#!/usr/bin/env python
# coding: utf-8

# # 1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# In[1]:


def myreduce(function,values):
    result=values[0]
    for i in values [1:]:
        result=function(result,i)
    return result


# In[4]:


def function(a,b):
    return a+b


# In[5]:


l=[1,2,3,4,5]
print(myreduce(function,l))


# # 2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[6]:


def myfilter(func,value):
    result=list()
    for i in value:
        if func(i):
            result.append(i)
    return result       
    


# In[7]:


def func(num):
    if num%2==0:
        return True
    else:
        return False
    


# In[8]:


lst=[12,34,5,6,7,91]
print(myfilter(func,lst))


# # 2. Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists

# #### 1.) ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

# In[9]:


lst=['x','y','z']
pattern=[i*row for row in lst for i in range(1,5)]
pattern


#  #### 2.) ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

# In[10]:


lst=['x','y','z']
pattern=[i*row for i in range(1,5) for row in lst ]
pattern


# #### 3.) [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[11]:


lst1=[1,2,3]
lst3=[(j,i) for i in lst1 for j in lst1]
lst3


# #### 4.) [[2], [3], [4], [3], [4], [5], [4], [5], [6]]

# In[12]:


lst4=[[x+y] for y in range(3) for x in range(2,5)]
lst4


# #### 5.)[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]

# In[14]:


lst5=[[x+y for y in range(2,6)] for x in range(4)]
lst5


# In[ ]:




