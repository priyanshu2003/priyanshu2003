#!/usr/bin/env python
# coding: utf-8

# # CS1101 Assignment - 3

# ## Question 1: 

# Write a python code that calculates the following sums in a single loop,
# $$ \sum_{i=1}^{n} i^{2}\ and\ \sum_{i=1}^{n} i^{3}$$
# Also calculate the expected answers by using the following:
# $$\sum_{i=1}^{n} i^{2} = \dfrac{1}{6} n (n+1) (2n+1)\ and\ \sum_{i=1}^{n} i^{3} = \dfrac{1}{4} n^{2} (n+1)^{2}$$
# 

# In[5]:


n = int(input("Enter a limit: "))
sum1 = 0
sum2 = 0
for i in range (1,n+1):
    sum1 = sum1 + i**2
    sum2 = sum2 + i**3
sum1f = (1/6) * (n) * (n+1) * (2*n + 1) 
sum2f = (1/4) * (n**2) * ((n+1)**2)
print ("First sum = %s" %(sum1))
print ("Second Sum = %s" %(sum2))
print ("For the first sum, are the results of the loop and formula the same?")
print("Answer: %s" %(sum1 == sum1f))
print ("For the second sum, are the results of the loop and formula the same?")
print("Answer: %s" %(sum2 == sum2f))


# ## Question 2:

#  Create a list of numbers having following pattern: $[1, 0, 3, 0, 5, 0, 7, 0, 9, \dots]$

# In[7]:


n = int(input("Enter a limit: "))
list = []
for i in range (1, (n+1), 2):
    list.append(i)
    list.append(0)
print (list)


# ## Question 3:

# Create a list of integers where nth item of the list is given by: $S_n = \sum_{i=1}^{n} i^{2} $

# In[11]:


n = int(input("Enter a limit: "))
list = []
sum = 0
for i in range (1, (n+1)):
    sum = 0
    for j in range (1, i+1):
        sum = sum + j**2
    list.append(sum)
print(list)


# ## Question 4:

# Calculate (using for loop) the value of : 
# $$1 + \dfrac{n}{1 + \dfrac{n-1}{1 + \dfrac{n-2}{1 + \dfrac{\dots}{1 + \dfrac{2}{1 + \dfrac{1}{1}}}}}}$$

# In[24]:


n = int(input("Enter a limit: "))
sum = 1
for i in range (1, (n+1)):
    frac = i/sum
    sum = 1 + frac
print(sum)


# ## Question 5:

# Write a program which prints the elements of a Fibonacci series $1, 1, 2, 3,5, 8, 13, \dots$, where each element is the sum of the two previous elements (the first two numbers are defined to be 1). 

# In[19]:


def fibonacci(num):
    num1 = 0
    num2 = 1
    fib = 0
    list = []
    for i in range(num):
        list.append(fib)
        num1 = num2
        num2 = fib
        fib = num1 + num2
    return (list)
num = int(input('Enter limit: '))
list1 = fibonacci(num)
list1.remove(list1[0])
print(list1)


# ## Question 6:

# Write a program that will compute the square root of a given number. If the input is a negative number, the program should print an error message that invalid input is provided and continue to take the inputs until a valid (positive) input is provided. 

# In[25]:


while(True):
    x = int(input('Enter a number'))
    if(x<0):
        print('Invalid Input. Try Again!')
    if(x>0):
        print("Square Root =", x**0.5)
        break


# ## Question 7:

# ### 7.1

# Take the name and age of a student as input and store them in a tuple. 

# In[26]:


name = input('Enter name')
age = input('Enter age')
x = (name, age)
print(x)


# ### 7.2

# Take the same information (name and age) of 10 students and make a list of tuples.

# In[28]:


list = []
for i in range (0,10):
    name = input('Enter name: ')
    age = input('Enter age: ')
    x = (name, age)
    list.append(x)
print(list)


# ### 7.3

# Take a name from the user as input and output the corresponding age.

# In[36]:


list = []

for i in range (0,10):
    name = input('Enter name: ')
    age = input('Enter age: ')
    x = (name, age)
    list.append(x)
    
def search(List, n):
    for i in range (0, len(List)):
        for j in range (0, len(List[i])):
            if (List[i][j]==n):
                print('Age: %s' %(List[i][j+1]))
                return (True)
    
name1 = input('Enter the name you want to search: ')
x = search(list, name1)
if (x):
    print('Name was found in list')
else:
    print('Invalid Input')


# ## Question 8:

# Write a program to find the digits which are absent in a given mobile number. 

# In[40]:


x = str(input('Enter a mobile number: '))
del list
char = list(x)
zero=0
one=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0
for i in range (0, len(char)):
    if(char[i]=='0'):
        zero+=1
    if(char[i]=='1'):
        one+=1
    if(char[i]=='2'):
        two+=1
    if(char[i]=='3'):
        three+=1
    if(char[i]=='4'):
        four+=1
    if(char[i]=='5'):
        five+=1
    if(char[i]=='6'):
        six+=1
    if(char[i]=='7'):
        seven+=1
    if(char[i]=='8'):
        eight+=1
    if(char[i]=='9'):
        nine+=1
if (zero==0):
    print('0 is absent')
if (one==0):
    print('1 is absent')
if (two==0):
    print('2 is absent')
if (three==0):
    print('3 is absent')
if (four==0):
    print('4 is absent')
if (five==0):
    print('5 is absent')
if (six==0):
    print('6 is absent')
if (seven==0):
    print('7 is absent')
if (eight==0):
    print('8 is absent')
if (nine==0):
    print('9 is absent')


# ## Question 9:

# Consider a list (rollnos) containing roll numbers of 20MS students in the format 20MSid (e.g. 20MS145, here id = 145). Use list comprehension to store the rollnos in a list 'GroupA' where id < 150 and store the rest in another list 'GroupB'. Print the contents of GroupA and GroupB.

# In[8]:


input_list = []
GroupA = []
GroupB = []
n = int(input('Enter no. of students: '))
for i in range (0, n):
    roll = input('Enter Roll No.: ')
    input_list.append(roll)
GroupA = [i for i in input_list if int(i[4]+i[5]+i[6])<150]
GroupB = [i for i in input_list if int(i[4]+i[5]+i[6])>=150]

print(GroupA)
print(GroupB)


# ## Question 10:

# Given the temperatures in Farenheit in a list 'farenheit', store the celsius equivalents in another list 'celsius' using list comprehension. You can choose the temperatures in the list farenheit. Take the length of the list to be 5. I am using the formula, $$^{\circ}C =\ (^{\circ}F-32) \times \dfrac{5}{9}$$

# In[3]:


farenheit = [0, 0, 0, 0, 0]
celsius = [0, 0, 0, 0, 0]
for i in range (0,5):
    x = float(input('Enter Farenheit Temperature: '))
    farenheit[i] = x
celsius = [(i-32)*(5/9) for i in farenheit]
print('The Celsius equivalents are:-')
print(celsius)


# ## Question 11:

# Store the marks of five courses CS1101, CH2201, CS3201, CS3202 and LS2201 in a tuple `marks`. Update `marks` by adding grace marks of 5 for the marks less than 50. 

# In[56]:


markslist = list(marks)
markslist[0] = int(input('Enter marks obtained in CS1101: '))
markslist[1] = int(input('Enter marks obtained in CS2201: '))
markslist[2] = int(input('Enter marks obtained in CS3201: '))
markslist[3] = int(input('Enter marks obtained in CS3202: '))
markslist[4] = int(input('Enter marks obtained in LS2201: '))
marks= tuple(markslist)
print(marks)
for i in range(0, 5):
    if (markslist[i]<50):
        markslist[i] = markslist[i] + 5
marks = tuple(markslist)
print('After adding the grace marks, the marks look like this:-')
print(marks)


# 
