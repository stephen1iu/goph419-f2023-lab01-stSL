import math
from math import factorial
import numpy as np

RADIUS = 6378100

def get_input():
    alpha=float(input("Enter the maximum altitude (m): "))
    tol_alpha=float(input("Enter tolerance for maximum altitude: "))
    ve_v0=float(input("Enter ratio of escape velocity to terminal velocity: "))  
    return(alpha,ve_v0,tol_alpha)

def arcsin(x):
    asin=0
    x=1
    for n in range (1,11,1):
        asin += (((2*x)**(2*n))/((n**2)*((math.factorial(n*2))/(math.factorial(n))**2)))
        asin=np.sqrt(asin)
    return(asin)

def launch_angle(ve_v0,alpha):
    sin_phi=(1+alpha)*(np.sqrt((1-((alpha/(1+alpha)*((ve_v0)**2))))))
    angle=arcsin(sin_phi)
    return(angle)

def launch_angle_range(ve_v0,alpha,tol_alpha):
    """Description of function.
    Parameters
    ----------
    Returns
    -------
    """

    lower=alpha-tol_alpha
    angle_lower=launch_angle(ve_v0,lower)
    upper=alpha+tol_alpha
    angle_upper=launch_angle(ve_v0,upper)
    #print(angle_lower,angle_upper)
    phi_range=0
    return (phi_range)

def start():
    alpha,ve_v0,tol_alpha=get_input()
    phi_range=launch_angle_range(ve_v0,alpha,tol_alpha)

start()
