import math
from math import factorial
import numpy as np
#import matplotlib.pyplot as plt

RADIUS = 6378100

def get_input():
    alpha=float(input("Enter the maximum altitude: "))
    tol_alpha=float(input("Enter tolerance for maximum altitude: "))
    ve_v0=float(input("Enter ratio of escape velocity to terminal velocity: "))  
    return(alpha,ve_v0,tol_alpha)

def arcsin(x):
    asin=0
    for n in range (1,16,1):
        asin += (((2*x)**(2*n))/((n**2)*((math.factorial(n*2))/(math.factorial(n))**2)))
    asin=asin/2
    asin=np.sqrt(asin)
    return(asin)

def launch_angle(ve_v0,alpha):
    sin_phi=(1+alpha)*(np.sqrt((1-((alpha/(1+alpha)*((ve_v0)**2))))))
    converion=180/np.pi
    angle=arcsin(sin_phi)*converion
    return(angle)

def launch_angle_range(ve_v0,alpha,tol_alpha):
    """Description of function.
    Parameters
    ----------
    Returns
    -------
    """
    #creating upper and lower bounds for alpha
    lower=((1-tol_alpha)*alpha)
    upper=((1+tol_alpha)*alpha)
    angle_lower=launch_angle(ve_v0,lower)
    angle_upper=launch_angle(ve_v0,upper)
    phi_range=np.array([angle_lower,angle_upper])
    print(phi_range)
    return (phi_range)

def main():
    alpha,ve_v0,tol_alpha=get_input()
    phi_range=launch_angle_range(ve_v0,alpha,tol_alpha)
    #holds ve_v0 and tol_alpha constant to show range of alpha values and their max and min angle ranges
    list_max=[]
    list_min=[]
    x_axis=alpha
    #y_axis=both max and min of angles
    ve_v0=2.0
    tol_alpha=0.04
    alpha=0
    #while min is >0 loop runs
    while phi_range[1]>32:
        phi_range=launch_angle_range(ve_v0,alpha,tol_alpha)
        list_max.append(phi_range[0])
        list_min.append(phi_range[1]) 
        alpha+=0.05

    print ("ve_v0 and tol_alpha constant test")
    print (list_max, list_min)

    #hold alpha and tol_alpha constant, shows range of ve_v0 and max and min angle values
    
    list_max=[]
    list_min=[]

    alpha=0.25
    tol_alpha=0.04
    ve_v0=1.3
    #while min is >0 loop runs
    while phi_range[1]>16:
        phi_range=launch_angle_range(ve_v0,alpha,tol_alpha)
        list_max.append(phi_range[0])
        list_min.append(phi_range[1])
        ve_v0+=0.05
    print("alpha and tol_alpha constant test")
    print(list_max, list_min)

if __name__=="__main__":
    main()
