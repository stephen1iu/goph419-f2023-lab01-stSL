import math
from math import factorial
import numpy as np
import matplotlib.pyplot as plt

def arcsin(x):
    """Description of function.
    Parameters
    x: input value (float or int)
    ----------
    Returns
    asin: arcsin of a value x (float or int) 
    -------
    """
    asin=0
    for n in range (1,16,1):
        asin += (((2*x)**(2*n))/((n**2)*((math.factorial(n*2))/(math.factorial(n))**2)))
    asin=asin/2
    asin=np.sqrt(asin)
    return(asin)

def launch_angle(ve_v0,alpha):
    """Description of function.
    Parameters
    ve_v0: Ratio of escape velocity to terminal velocity (float)
    alpha: Ratio of Earth's radius as an altitude (float)
    ----------
    Returns
    angle: angle from equation (17) and (18) in degrees (float)
    -------
    """
    sin_phi=(1+alpha)*(np.sqrt((1-((alpha/(1+alpha)*((ve_v0)**2))))))
    converion=180/np.pi
    angle=arcsin(sin_phi)*converion
    return(angle)

def launch_angle_range(ve_v0,alpha,tol_alpha):
    """Description of function.
    Parameters
    ve_v0: Ratio of escape velocity to terminal velocity (float)
    alpha: Ratio of Earth's radius as an altitude (float)
    tol_alpha: Tolerance for alpha (float)
    ----------
    Returns
    phi_range: array of max and min allowed angles (array/list) 
    -------
    """
    #creating upper and lower bounds for alpha
    lower=((1-tol_alpha)*alpha)
    upper=((1+tol_alpha)*alpha)
    angle_lower=launch_angle(ve_v0,lower)
    angle_upper=launch_angle(ve_v0,upper)
    phi_range=np.array([angle_lower,angle_upper])
    #print(phi_range)
    return (phi_range)

def main():
    #holds ve_v0 and tol_alpha constant to show range of alpha values and their max and min angle ranges
    list_alphamax=[]
    list_alphamin=[]
    #values solved for from boundary cases
    alpha_values=np.arange(0,0.333333,0.05)

    for i in alpha_values:
        phi_range=launch_angle_range(2.0,i,0.04)
        list_alphamax.append(phi_range[0])
        list_alphamin.append(phi_range[1])

    plt.plot(alpha_values,list_alphamax,label="Maximum Angle")
    plt.plot(alpha_values,list_alphamin,label="Minimum Angle")
    plt.title("Range of Altitudes and Respective Max and Min Angles")
    plt.xlabel('Alpha (m)')
    plt.ylabel('Angles (degrees)')
    plt.legend()
    plt.savefig('../../figures/plot_1.png')
    plt.show()

    #hold alpha and tol_alpha constant, shows range of ve_v0 and max and min angle values
    list_alphamax=[]
    list_alphamin=[]
    #values solved for from boundary cases
    ve_v0_values=np.arange(1.3,2.2,0.1)

    for i in ve_v0_values:
        phi_range=launch_angle_range(i,0.25,0.04)
        list_alphamax.append(phi_range[0])
        list_alphamin.append(phi_range[1])
        
    plt.plot(ve_v0_values,list_alphamax,label="Maximum Angle")
    plt.plot(ve_v0_values,list_alphamin,label="Minimum Angle")
    plt.title("Range of Velocity Ratios and Respective Max and Min Angles")
    plt.xlabel('Ratio of Escape Velocity to Terminal Velocity')
    plt.ylabel('Angles (degrees)')
    plt.legend()
    plt.savefig('../../figures/plot_2.png')
    plt.show()

if __name__=="__main__":
    main()
