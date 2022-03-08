#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1
operation=1
while operation in [1,2,3,4]:
    print('*******Calculator*******','\n','1 - Addition','\n','2 - Subtraction','\n','3 - Multiplication','\n','4 - Division','\n','Any other number to exit')
    operation=int(input('Enter your choice:'))
    if operation in [1,2,3,4]:
        print('Enter the two operands:')
        a=float(input('Enter 1st operand:'))
        b=float(input('Enter 2nd operand:'))
        if operation==1: print('Result=',a+b)
        if operation==2: print('Result=',a-b)
        if operation==3: print('Result=',a*b)
        if operation==4: print('Result=',a/b)
    else: print('Exiting')


# In[10]:


#Q2
def f(x,y):
    print ('The distance between them is:',  ((float(x[1])-float(y[1]))**2 + (float(x[0])-float(y[0]))**2)**0.5)
f(x=input('Enter point 1 coordinates (space separated):').split(' '),y=input('Enter point 2 coordinates (space separated):').split(' '))


# In[12]:


#Q3
n=input('Enter the number of Wins, Losses, Draws (Space Separated):').split(' ')
print('Team point(s) =',int(n[0])*2+int(n[2]))


# In[13]:


#Q4
D=input('Enter DNA Sequence:')
R=str()
for i in D:
    if i=='T': R+='U'
    else: R+=i
print('The corresponding RNA Sequence is',R)


# In[14]:


#Q5
d=input('Enter DNA sequence:')
A=0
T=0
G=0
C=0
for i in d:
    if i=='A': A+=1
    if i=='T': T+=1
    if i=='G': G+=1
    if i=='C': C+=1
print(f'A:{A},T:{T},G:{G},C:{C}')


# In[15]:


#Q6
wd=(' ').join(sorted(list(set(input('Enter words separated by spaces:').split()))))
print(wd)


# In[17]:


#Q7
lst = ['I','think','therefore','I', 'am','said','Rene','Descartes']
dct = {'Rene' : 0, 'Descartes' : 1, 'I' : 2, 'think': 3}
K=input('Enter key K:')
if K in set(lst)&set(dct):
    print(f'Value of {K} in dictionary is', dct[K])
else: print(f'{K} not found in either list or dictionary')


# In[ ]:




