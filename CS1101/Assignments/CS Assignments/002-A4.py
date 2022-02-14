#!/usr/bin/env python
# coding: utf-8

# # CS1101 Assignment - 4

# ## Question 1: 

# Write a program to flatten a given nested list structure.
# 
# Input: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# 
# Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# 

# In[3]:


input_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120, [10, 20,[10,20,[20,30]]]], [[1,2,3,4,5],[6,7,8,9,10]]]
final = []
print("Original list is:",input_list)
def flatten(list1):
    for i in list1:
        if(type(i) == type(final)):
            flatten(i)
        else:
            final.append(i)
flatten(input_list)
print("flattened list is:",final)


# ## Question 2:

#  Take two integers R and C (as user input) and initialise a Matrix of dimension R × C taking 
# the values from the user using nested lists. Each of the R rows will be stored in lists and all 
# the rows will be individual elements in a list. The individual input elements will be in the 
# range (-999, 999). Print the matrix. 

# In[31]:


m = int(input("Enter no. of rows: "))
n = int(input("Enter no. of columns: "))
arra = []
for i in range (0,m):
    sublist = []
    for j in range (0,n):
        t = input("Enter element in row %s and column %s: " %(j+1, i+1))
        sublist.append(t)
    arra.append(sublist)
    
for i in range(0,m):
    for j in range(0, len(arra[i])):
        print('%s ' %(arra[i][j]), end=' ')
    print()


# ## Question 3:

# Given a list of values, write a program that removes duplicates from the list.
# 
# Input: [3, 7, 13, 9, 7, 5, 13, 17, 23, 17, 7, 29]
# 
# Output: [3, 7, 13, 9, 5, 17, 23, 29]
# 
# Input: ["A", "E", "E", "O", "A"]
# 
# Output: ["A", "E", "O"]
# 

# In[12]:


list1 = []
n = int(input("Enter desired length of list: "))
for i in range (0,n):
    x = input("Enter list item: ")
    list1.append(x)
final =[]
def duplicate(list):
    for i in list:
        if i not in final:
            final.append(i)
    return final


output = duplicate(list1)
print("After removing duplicates: ", output)


# ## Question 4: 

# ### 4.1

# Take a set of non-zero integers from the user as input until the user enters 0. Store the inputs in a list. 

# In[39]:


input_list  = []

while(True):
    x = input("Enter an integer: ")
    if (any(map(str.isdigit, x)) and int(x)!=0):
        input_list.append(x)
    elif (int(x)==0):
        print("You have entered zero, so the loop termintes")
        break
    else:
        print("Please enter an integer next time")
        break
print(input_list)

# the program results in an error if the user enters an alphabet/spl. character/float 


# ### 4.2

#  Compute the average of the input numbers. 

# In[40]:


S = 0
for i in range (0,len(input_list)):
    S = S + int(input_list[i])
avg = S/len(input_list)
print('Average =', avg)


# ## Question 5: 

# ### 5.1

# Make a list called `numbers` containing all the numbers from 1 to 100. 

# In[43]:


numbers = [i for i in range(1,101)]


# ### 5.2
# 
# Make another list `squares` that would contain each number from the list `numbers` followed by its square. i.e. `squares` should look like this: `squares=[1,1,2,4,3,9,4,16,….,100,10000]`
# 

# In[50]:


square = [i**2 for i in numbers]
squares = []
for i in range (0,100):
    squares.append(numbers[i])
    squares.append(square[i])
print(squares)


# ## Question 6:

# Take the dictionary called squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}. Using a loop modify squares by 
# adding 4 more items to it 6:36, 7:49, 8:64, 9:81 and print out the modified dictionary. Remove the 
# first key from the modified squares and print out the value associated with the key.
# 

# In[63]:


squares =  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares.update({6:36, 7:49, 8:64, 9:81})
x = squares.get(1)
del squares[1]
print ("Element Removed: ", x)
print("Dictionary afer removing elements:", squares)


# ## Question 7: 

# Take a nested list of the form `arra = [[1, 2, 3, 4],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]`. Write a 
# code to remove the last element of each nested list item (example: 4 from the first list, 7 from the 
# second, etc.) and print the modified nested list. 

# In[68]:


m = int(input("Enter length of outer list: "))
n = int(input("Enter length of sublists: "))
arra = []
for i in range (0,m):
    sublist = []
    for j in range (0,n):
        t = input("Enter element no. %s of sublist no. %s: " %(j+1, i+1))
        sublist.append(t)
    arra.append(sublist)
    
print("List before deleting elements: ", arra)

for i in range (0,m):
    del arra[i][n-1]
    
print("List after deleting elements: ", arra)


# ## Question 8:

# Given a dictionary, write a program to find the sum of all values in the dictionary. You can choose the following dictionaries to test your code or make your own. Note that the values associated with the keys should be numbers and cannot be strings.
# 
# Input: ’a’: 100, ’b’:200, ’c’:300
# 
# Output: 600
# 
# Input: ’x’: 25, ’y’:18, ’z’:45
# 
# Output: 88
# 

# In[7]:


n = int(input("Enter the limit"))
dicti = {}
for i in range (0,n):
    key = input("Enter key %s: " %(i+1))
    value = int(input('Enter value %s: ' %(i+1)))
    dicti[key] = value
print(sum(dicti.values()))


# ## Question 9:

# Consider the following tuple of tuples (t_o_t)
# `t_o_t = (('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'), ('sun', 'mon', ‘tue’, 'wed', 'thu', 'fri', 'sat'))`
# Using appropriate indexing of the tuple `t_o_t`, extract and print the items ‘apr’, ‘fri’ from `t_o_t`.
# Then print following items in the given order: `jan, ('sun', 'mon', ‘tue’, 'wed', 'thu', 'fri', 'sat')`
# 

# In[10]:


t_o_t = (('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'), ('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'))
print(t_o_t[0][3], t_o_t[1][5], sep=', ')
print(t_o_t[0][0], t_o_t[1], sep=', ')


# ## Question 10:

# Given a list, convert it into a dictionary by mapping alternate elements as key-value pairs.
# 
# If you use the following list as input: `lst = [2, 3, 5, 6, 7, 8]` for testing the code.
# 
# Output: `{2: 5, 3: 6, 5: 7, 6: 8}`

# In[12]:


lst = []
n = int(input('Enter limit: '))
for i in range (0,n):
    x = input("Enter element no. %s: " %(i+1))
    lst.append(x)
dicti = {}
for i in range (0,n):
    if (i<n-2):
        dicti[lst[i]] = lst[i+2]
print(dicti.items())


# In[ ]:




