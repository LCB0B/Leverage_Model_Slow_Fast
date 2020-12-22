# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:33:12 2020

@author: boucher
"""

#################### PLOT #########################



fig = plt.figure(figsize=(5,5))
fig.subplots_adjust(wspace = 0.5, hspace = 0.3)
ax1 = fig.add_subplot(5,1,1)
ax2 = fig.add_subplot(5,1,2)
ax3 = fig.add_subplot(5,1,3)
ax4 = fig.add_subplot(5,1,4)
ax5 = fig.add_subplot(5,1,5)

n = int(T/dt)
t = np.linspace(0,T,n)

#lambda_ = alpha * (x[:,4] + s_0)**b
w = 0.5
#A = x[:,2]*x[:,3]/w

T1 = 100
T2 = 300
#xx= np.array([x[500*i] for i in range(int(len(x)//1000))])
#t = np.array([t[500*i] for i in range(int(len(t)//1000))])
lambda_ = x[:,4]

tau = 1
#ax1.plot(t,10*(A-x[:,1])/x[:,2], 'r-',label ='W')
ax1.plot(tau*t,x[:,0], 'k-',label ='W')
ax1.set_ylabel(r'$W$')


#ax2.plot(t,(1-1/lambda_)*x[:,2]*x[:,3]/w, 'k',label ='L',alpha = 0.2)
ax2.plot(tau*t,x[:,1], 'k-',label ='L')
#ax2.plot(t,x[:,1]-(lambda_-1)*E, 'b-',label ='L')
ax2.set_ylabel(r'$L$')



###### AX3 P ######

ax3.plot(tau*t,x[:,2], 'k-',label ='p')



###### AX4 ######

ax4.plot(tau*t,x[:,3], 'k-',label ='n')
#ax4.plot(t,w/x[:,2] * (E+x[:,1]), 'r--',alpha=0.4)
ax4.set_ylabel(r'$n$')


#ax5.plot(t,A/E, 'k--',label ='s',alpha=0.5)
ax5.plot(tau*t,lambda_, 'k-',label ='s')

#ax5.plot(t,(np.log(1-theta*lambda_*(E*(lambda_-1)-x[:,1]) / (x[:,1]+10)))**2, 'g--',label ='s')
ax5.set_ylabel(r'$ \lambda $')
ax5.set_xlabel(r'$ t $')

#ax1.set_ylim([0,1])
#ax2.set_ylim([0,1])
#ax3.set_ylim([0,1])
#ax4.set_ylim([0,1])
#ax5.set_ylim([0,1])

plt.grid()
plt.show()