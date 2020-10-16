#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[ ]:


x = int(input("Enter a value for x:"))
y = int(input("Enter a value for y:"))

vec1 = np.array([x,y])
vec2 = np.array([-x, -y])

def add (x, y):
    return x + y

def mult (x, y):
    return x*y

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

