import math
from math import factorial
import numpy as np

RADIUS = 6378100

def get_input():
    answer_good=False
    while (answer_good)==False:
        alphaR=input("Enter the maximum altitude (m): ")
        alpha=alphaR/RADIUS
        ve=input("Enter escape velocity (m/s): ")
        v0=input("Enter terminal velocity (m/s): ")
        ve_v0=ve/v0
        answer_good=True
    return(alpha,ve_v0)

def arcsin(x,n):
    asin=0
    x=1
    for n in range (1,20,1):
        asin += (((2*x)**(2*n))/((n**2)*((math.factorial(n*2))/(math.factorial(n))**2)))
        asin=np.sqrt(asin)
    print (asin)

def launch_angle():
    pass 

def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Description of function.
    Parameters
    ----------
    Returns
    -------
    """



    return (phi_range)

def start():
    x=0
    n=20
    arcsin(x,n)

start()