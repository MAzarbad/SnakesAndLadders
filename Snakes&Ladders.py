#!/usr/bin/env python
# coding: utf-8

import sympy as sp
import numpy as np
sp.init_printing()

snakeheads = np.array([27,55,61,69,79,81,87,91,95,97])
snaketails = np.array([10,16,14,50,5,44,31,25,49,59])

ladder1    = np.array([6,8,13,20,33,37,41,57,66,77])
ladder2    = np.array([23,30,47,39,70,75,62,83,89,96])

st1 = np.append(snakeheads, ladder1)
st2 = np.append(snaketails, ladder2)

def marplle(n):
    if any(st1==n):
        return(st2[st1==n][0]) 
    else: return(n) 

M = np.matrix(np.zeros([100,100],dtype=int))
for j in range(100):
    if not any(snakeheads == j+1):
        jj = np.array([marplle(n) for n in j+1+np.arange(1,7)])
        m = np.sum(jj>100)
        M[j, np.append(j,jj[jj<=100]-1)] = np.append(m,np.ones(6-m))


p0 = np.matrix(np.append(1,np.zeros(99,dtype=np.int)))

def prob(n):
    return sp.Matrix(p0*M**n)/6**n


# Probability distribution when you roll the dice 10 times 

p10 = prob(10)
p10


# Example: When you roll the dice 10 times, what is the probability of being on position 12? 

p10[11]


n=1000
A = np.matrix(p0, dtype=np.double)
P1 = np.matrix(M, dtype=np.double)/6
T=np.zeros(n, dtype=np.double)
for j in range(n):
    B=A*P1
    T[j]=B[0,99]-A[0,99]
    A=B


np.sum(T)


# What is the probability of finishing the game by 14 dice rolls? 
T[13]


# In[18]:


prob(14)[99]-prob(13)[99]


# What is the minimum number of dice roles needed to finish the game? 

sum(T == 0)


# Expected value of number of dice roles needed to finish the game? 

ET=sum(np.arange(1,n+1)*T)
ET


# Simulation of the game.

def GAME():
    j = 1
    Game = [1]
    while j<100:
            a = marplle(j+np.random.choice(range(1,7)))
            if a <= 100: j = a
            Game = Game + [j]
    return Game



GAME()

