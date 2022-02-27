#!/usr/bin/env python
# coding: utf-8

# # CS1101 Assignment - 5

# ## Question 1:

# Write a program which takes two integers from the user and returns all prime numbers
# between the two integers. The result should not depend on the order in which the integers 
# are entered by the user.

# In[4]:


x = int(input("Enter a number: "))
y = int(input("Enter a  number: "))

def checkPrime(s):
    c = 0
    for i in range (1,s+1):
        if (s%i==0):
            c+=1
    if(c==2):
        return s
    else:
        return ('')

print('The prime numbers in the range are: ')
for i in range (min(x,y), max(x,y)):
    print(checkPrime(i))


# ## Question 2:

# The exponential of a functon is given by: $e^{x} = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots$
# 
# In general, the $n^{th}$ term is: $\frac{x^{n}}{n!}$
# 
# Since the evaluation of n! is time intensive for large n, another way out is to note the existence of a recursive relation:
# $$T_n = \frac{x}{n} \cdot T_{n-1}$$
# 
# where, $T_{n}$ is the $n^{th}$ term of the series. We may calculate $e^{x}$ efficiently by using the above relation.
# 
# Write a program which uses the above relation to evaluate $e^{\pi}$ to the accuracy of $10^{-4}$. 
# Your program should print number of terms of the series (which have been evaluated), the computed value, the actual value and their absolute difference of the two.

# In[11]:


import math
e = math.e
pi = math.pi
actual = e**pi
S = 0
term = 1
counter = 0
n=1
while round((abs(S - actual)),4)>0.0001:
    S = S + term
    term = (pi/n)*term
    counter = counter + 1
    n += 1
print('Actual Value:', actual)
print('Value using expansion:', S)
print('No. of terms considered: ', counter)
print('Difference between the values:', abs(S-actual))


# ## Question 3:

# Use the above method (relation between successive terms) to estimate $\sin (\frac{\pi}{2})$ to the accuracy of $10^{-4}$. Your program should print number of terms of the series (which have been evaluated), the computed value, the actual value and their absolute difference of the two. You can use the series expansion:
# $$\sin(x) = x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}-\dfrac{x^7}{7!}...
# =\sum_{n=0}^{\infty} \dfrac{(-1)^n x^{2n+1}}{(2n+1)!}$$

# In[13]:


import math
pi = math.pi
#sin(pi/2)=1
def a_sin(x,n):
    if n==0:

        return x
    else:
        return -(x**2 * a_sin(x,n-1))/(4*n**2 + 2*n)

epsilon=10**-4
S=0
n=0
while(abs(1-S)>=epsilon):
    S+=a_sin(pi/2,n)

    n+=1
print(f"Actual value = 1")
print(f"Computed value = %s "%(S))
print(f"Error = {abs(1-S)}")
print(f"No of terms = {n}")


# ## Question 4:

# Write a code to generate the following pattern. You can define x = 'A' and y = ' ' and use them to generate the pattern:
# 
# ![AA.png](attachment:AA.png)

# In[64]:


x = 'A'
y = ' '
n = int(input('Number of A\'s you want in the last row: '))
if (n%2 != 0):
    hlf = int(((n-1)/2)+1)
else:
    hlf = int((n/2)-1)
for i in range (hlf, 0, -1):
    for j in range (0,i):
        print(y, end='')
    if (n%2 !=0):
        for k in range (0, n-2*i):
            print(x,end='')
    if (n%2 ==0):
        for k in range (0, n-2*i):
            print(x,end='')
    print()


# ## Question 5:

# Suppose the length of three sticks are given by three numbers. Define a function which
# takes the three lengths (as arguments) and determines whether these sticks can form a 
# triangle. The function should return True or False depending on whether the triangle is 
# formed or not. Your program should take three numbers from the user and should print 
# whether a triangle is possible or not. For a triangle to be formed out of 3 lengths, the sum of 
# length of 2 sides must be greater than the length of the other side.

# In[89]:


print('Enter the length of 3 sides of a triangle')
x = input('First Side: ')
y = input('Second Side: ')
z = input('Third Side: ')
res = False
if (((x+y)>z) or ((x+z)>y) or ((y+z)>x)):
    res = True
print('Can a triangle be made out of these side lengths ? ')
print('Answer:', res)


# ## Question 6:

# The following series yields the value of $$\arctan (x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1} }{2n + 1}$$.
# 
# Define a function f(x, n) which calculates the above series up to nth term for a given x. Write 
# a program which finds the number of terms required to compute the value of $\pi$ (using the 
# above series) correct up to an absolute difference of $10^{-3}$
# . The program should print the 
# number of terms required (value of n), the exact value of $\pi$, the computed value of $\pi$ and 
# their absolute difference.
# 

# In[1]:


import math
from decimal import Decimal
from decimal import *


def series(x, n):
    actual = math.atan(x)
    S = 0
    term = 0
    counter = 0
    for i in range (1, n*2, 2):
        term = ((-1)**counter * 1**i)/(i)
        S = S + term
        counter += 1
    return(S, abs(S-actual), counter)
    
for i in range (1, 1000001):
    x,y,c = series (1, i)
    if (y < 10**(-4)):
        print('Actual Value of pi is: ' , 4*math.atan(1))
        print('Final value of pi from series:',4*x)
        print('Difference between the two:', ((4*math.atan(1)) - 4*x))
        print('Minimum number of iterations required for an accuracy of less than 10^-3:', c)
        break


# ## Question 7:

# Define a function which takes a number (x) as argument and returns the 9/10 power of 
# the same number ($x^{0.9}$). If x is greater than 1, then $f(x) < x$ and $f(f(x)) < f(x)$. Let us suppose, 
# that we start with $x = 10$ and in each iteration, we assign $x = f(x)$. How many iterations do we 
# need to perform to have $x < 2$ starting from $x = 10$?

# In[27]:


def f(x): return(x**0.9)
x = 10
i = 0
print("Value of x changes as:")
while(x):
    print(x)
    x = f(x)
    if (x<2): 
        x = f(x)
        print(x)
        break
    i += 1
print("\nThe function was executed on x,",i,"number of times, to reach less than 2 from 10.")


# In[ ]:





# In[ ]:




