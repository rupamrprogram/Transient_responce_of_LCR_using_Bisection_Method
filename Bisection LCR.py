# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:59:23 2023

@author: dasru (Rupam Das)
"""

# Question
#The Swith in LCR circuit is thrown at a certain position for sufficientl long time to establish the full of DC voltage across capacitor C, then the switch is thrown back to the another position to discharge it through the resistance and inductance, R and L resprctively. This circuit design problem requires finding the resistance for which the capacitor is discharged to 1% of its original values at the time o.5 sec using the nbisection method. The function or R the only unknown variable.
#Importing Libaries
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import signal
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import *
import seaborn
from IPython.display import Image
#Find out the roots of the function using Bisection method



def bisection_method(f, R_lower, R_upper,L,C,q0,q,tolerance, max_iterations):
    if f(R_lower) * f(R_upper) >= 0:
        raise ValueError("The function values at the endpoints must have opposite signs.")

    # Initial values
    iteration = 0
    absolute_error = R_upper - R_lower 
    relative_error = 1

    while absolute_error > tolerance and relative_error > tolerance and iteration < max_iterations:
        R_mid = ( R_lower + R_upper) / 2
        if f(R_mid) == 0:
            break

        if f( R_lower) * f(R_mid) < 0:
            R_upper = R_mid
        else:
             R_lower = R_mid

        # Update errors
        absolute_error = R_upper - R_lower
        relative_error = absolute_error / R_upper

        iteration += 1

        print("Iteration:", iteration)
        print("Approximation 0f Resistor:", R_mid)
        print("Absolute Error:", absolute_error)
        print("Relative Error:", relative_error)
        print()
    return R_mid










#Define Function
# Example usage
def f(R):

    print()
    return (np.exp((R*t)/2*L) * (np.cos ((1/L*C)-((R/2*L)**2)*t)**0.5)) -(q/q0)
#Decleare the value of the variabl
R_lower = 200
R_upper = 400
tolerance = 0.0001
max_iterations = 10
L= 5                 #Inductance in Henry
C= 100 * 10 ** -6    #Capacitance In Farad
q0= 100              #Maximum charge in coulomb
q= 1                 #Ammount of discharge in coulomb
t= 0.05              #Time in second

root = bisection_method(f, R_lower, R_upper,L,C,q0,q,tolerance, max_iterations)

print("Root:", root)
value_of_function = f(root)
print ("The valuse of function", value_of_function)
R_values = np.linspace(R_lower,R_upper, 1000)
f_values = f(R_values)
plt.plot(R_values, f_values)
plt.xlabel('R in Ohm')
plt.ylabel('f(R)')
plt.grid(True)
plt.show()

R_values = np.linspace(0,10,100)
f_values = f(R_values)
plt.plot(R_values, f_values)
plt.legend()
plt.xlabel('R in Ohm')
plt.ylabel('f(R)')
plt.grid(True)
plt.show()
omega = 1/ np.sqrt(L*C)
print("Angular Frequency" , omega)
freq = omega /( np.pi * 2 )
print(" frequency of oscillaion", freq)