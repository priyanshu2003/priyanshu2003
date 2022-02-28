#!/usr/bin/env python
# coding: utf-8

# # CS1101 Assignment - 6

# ## Question 1:

# Define a function which takes n as an argument and evaluates $$g(n) = \sum_{i=1}^{n} \frac{i}{i+1}$$
# Print the values of g(n) for n = 1 to 20.
# 

# In[1]:


def series(n):
    S = 0
    term = 0
    for i in range(1, n+1):
        term = i/(i+1)
        S = S + term
    return S


for i in range(1, 21):
    print("g(%s) = " % (i), series(i))


# ## Question 2:

# Define a function which calculates the factorial of a given number. Show the usage of the function 
# by calculating the factorials from $n=1$ to $8$.

# In[1]:


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


for i in range(1, 9):
    print("%s! =" % (i), fact(i))


# ## Question 3:

# If you need to evaluate mathematical operations (log, sin, cos etc), you need to declare ``from math import *`` at the beginning of your program. For example, to find the value of cosine of $60 ^\circ$, your program should look like:
# 
#     from math import *
#     print cos(60*pi/180)
# 
# pi gives you the value of $\pi$ and $\theta \dfrac{\pi}{180}$ converts $\theta$ from degree to radian.

# Define a function which takes an argument $t$ and returns $\sin 2t$. Next write a loop which uses the 
# function to print θ, sin 2θ for θ = 0, 10, 20, 30, . . . , 80, 90.
# 

# In[6]:


from math import *


def doubleangle(t):
    d = 2*t
    return sin(d)


for i in range(0, 91, 10):
    print("%s, sin(2*%s) =" % (i, i), doubleangle(i))


# ## Question 4:

# Write a program to take a line of text as input; decipher the text by interchanging the odd positions characters with the even position characters.
# 
# Input: Enter a text: Satyajit Ray
# 
# Output: The result is: aSytjatiR ya
# 
# Input: Enter a text: Covid19 Vaccine
# 
# Output: The result is: oCiv1d 9aVccnie
# 

# In[17]:


x = input("Enter a text: ")
y = list(x)
l = len(x)
for i in range(0, l-1):
    if i % 2 == 0:
        temp = y[i]
        y[i] = y[i+1]
        y[i+1] = temp
print("Output: ", ''.join(y))


# ## Question 5:

# Write a program that takes a string as input and removes what is inside the brackets.
# 
# Input: Enter a string: Indian Statistical Institute (ISI) is a public research university.
# 
# Output: Indian Statistical Institute is a public research university.

# In[32]:


import re

n = str(input("Enter a text: "))
nt = re.sub("\(.*?\)", '', n)
print(nt)


# ## Question 6:

# Write a program that takes an integer N and then would take N positive integers as input into a list. Then count the number of even and odd numbers from a series of numbers.

# In[34]:


l = []
n = int(input("Enter the number of integers you want to consider: "))
for i in range(0, n):
    x = int(input("Enter a positive integer (%s): "%(i+1)))
    l.append(x)

even, odd = 0, 0

for i in l:

    if i % 2 == 0:

        even += 1

    else:

        odd += 1

print("No. of Even Numbers : ", even)

print("No. of Odd Numbers : ", odd)


# ## Question 7:

# Write a program to find the sum of the following series, given an integer n: 3 + 33 + 333 + 3333 + ... upto n terms.
# 
#     Input: Enter an integer: 6
#     Output: The result is: 370368
#     Input: Enter an integer: 9
#     Output: The result is: 370370367

# In[27]:


n = int(input("Enter the range of number:"))
sum = 0
p = 3
for i in range(1, n+1):
    sum += p
    p = (p*10)+3
print("The sum of the series = ", sum)


# ## Question 8:

# A strong number where the sum of the factorials of the digits making up the number is the 
# number itself. 
# 
# Example: 145=1!+4!+5!. 
# 
# Write a program to generate all strong numbers between 1 and 100,000.

# In[35]:


# function to find factorial
def fact(n):
    f = 1

    for i in range(1, n+1):
        f *= i

    return f


# function to check strong
def is_strong(n):

    if n < 0:
        return False

    number_copy = n
    strong_sum = 0

    while n:
        remainder = n % 10
        strong_sum += fact(remainder)
        n //= 10

    return strong_sum == number_copy


min_value = 1
max_value = 100000

# Looping & displaying if it is Strong
print('Strong numbers from %d to %d are:' % (min_value, max_value))
for i in range(min_value, max_value+1):
    if is_strong(i):
        print(i)


# In[ ]:




