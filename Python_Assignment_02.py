#!/usr/bin/env python
# coding: utf-8

# ### 1. Create the below pattern using nested for loop in Python.

# In[51]:


n = 5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i,n):
        print('',end='')
    print('\t')
for i in range(n):
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i+1):
        print('',end='')  
    print('\t')


# ### 2. Write a Python program to reverse a word after accepting the input from the user.

# In[54]:


word = input("Input word:")
"{}".format(word[::-1])


# In[ ]:




