# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy import linalg as LA
import time

#### FUNCTION  #####

def function(y,E,theta,eta,w,delta,alpha,s_0,b,rho,tv):
    
    mu = 25
    W,L,p,n,lambda_ = y 
    
    A = p*n/w
    
    #dot_W = x[0]*rho*((mu/x[2]-1)+float(np.random.normal(0,0.22,1)))
    dot_W = W*rho*((mu/p-1))
    #dot_W = 0
    dot_L = (theta*(lambda_*(A-L)-A))
    #dot_L = theta*(lambda_*(E*lambda_-x[1])-E*lambda_ )
    
    dot_p = (p* (1-n) * dot_W / W + eta*(w-W)*(E-A+L)+ w*dot_L ) / (1-n*w-(1-n)*W)
    #dot_p = ( eta*(w-x[0])*(E-A+x[1])+ w*dot_L ) 
    # / (1-x[3]*w-(1-x[3])*x[0])
    dot_n = n* (-(1-w)*dot_p/p + 1/A*(eta*(E-A+L)+dot_L))

    #dot_s = -delta*(x[4]) + delta * (np.log(1-dot_p/x[2]))**2
    #dot_s = -delta*(x[4]) + delta * (np.log(1-dot_p/x[2]))**2
    #dot_s = -delta*(s) + delta * tv**2*(-dot_p/p)**2
    a1 = w/p * theta * (A - L) / (1-n*w-(1-n)*W)
    a0 = (theta*n-(1-n)*rho*(mu/p-1)-eta/p*(w-W)*(E-A+L)) / (1-n*w-(1-n)*W)

    dot_lambda = lambda_*delta/2 * (1- (lambda_/alpha)**2 * (s_0 + tv**2*(a1*lambda_-a0)**2))

    return([dot_W, dot_L, dot_p, dot_n, dot_lambda])
    
    
def sys(iv, dt, time,function,E,theta,eta,w,delta,alpha,s_0,b,rho,tv, scale_v):
    n = int(time/dt)
    t = np.linspace(0,time,n)
    x = np.array([[ i for i in iv]]*n)
    n_ord = len(iv)
    
    #scale_v = np.array([w,2*theta,mu,w,theta])
    
    #scale_v = np.array([1,1,1,1,1])
    a = iv/scale_v

    
    
    for i in range(1,n):
        X = function(a*scale_v,E,theta,eta,w,delta,alpha,s_0,b,rho,tv)
        X[0] = X[0] 
        a = a + (np.array(X)*dt)/scale_v 
        #print('a = ',a)
        x[i] = a
    return np.array(x)

#### PARAMETERS #####
    
rho= 0.1
#rho = 100

E = 2
mu = 25
theta = 10
eta = 10
w = 0.5

#tv = 10**-1
#alpha = 10**-2
#s_0 = 10**-6
tv = 10**-1
alpha = 0.01
s_0 = 10**-6
#s_0=0

b = -0.5
#### 
T = 100
dt = 10**-4
delta = 0.5

p0 = 25
L0 = 20



#x= sys([0.2,L0,p0,0.5,1], dt,T,function,E,theta,eta,w,delta,alpha,s_0,b,rho,tv)
#ss = (alpha/0.1)**2-10**-6

scale_v = np.array([0.449,16.30,30.39,0.30,9.178])
scale_v = nscale_v = np.array([0.08367570934367924,18.025539887517258,13.782762702144932,0.29302765940913145,9.057653504809467])


scale_v = nscale_v = np.array([1,1,1,1,1])

#################### RUN #########################
start_time = time.time()


x= sys([0.3,-4,30,1,0.1], dt,T,function,E,theta,eta,w,delta,alpha,s_0,b,rho,tv, scale_v)

print("--- %s seconds ---" % (time.time() - start_time))


n = int(T/dt)
t = np.linspace(0,T,n)




