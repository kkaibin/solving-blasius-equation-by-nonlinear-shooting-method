"""
Created on TUE May 8 2018
@author: lab225/Neil
"""
#solve an ODE-BVP with non-linear shooting method
'''
lecture notes 4-15
'''

#use modules
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

########## Define function and Parameters ########## 
def fun(t, y): return [
        y[1],
        y[2],
        -0.5*y[0]*y[2],
        y[4],
        y[5],
        -0.5*y[2]*y[3]-0.5*y[0]*y[5]
        ]

t0=0
t_bound=10

y_left=0
y_right=1

i=0

solve='RK45' #choose method: RK45, LSODA or others

h=0.5
####################################################
  
step=int((t_bound-t0)/h+1)
T=np.array(range(step))
TT=T*h+t0
    
#for k in range(1,7,1):
 
y_try=10000
i=0
a=0.1
while abs(y_try-y_right)>10e-6:
    y0=[y_left,0,a,0,0,1]
    sol = solve_ivp(fun, [t0,t_bound],y0,method=solve,t_eval=TT,atol=1e-1)
    #print(sol.y[1])
    a=a-(sol.y[1][step-1]-y_right)/(sol.y[4][step-1])
    y_try=sol.y[1][step-1]
    i=i+1

for k in range (0,21,1):
    print(sol.y[2][k])

    
    

print("t_bound",t_bound,"a=",a,"iterate",i,"times")

plt.plot(sol.t,sol.y[2],"g--")
plt.show


