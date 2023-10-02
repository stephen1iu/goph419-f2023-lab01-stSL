from range import launch_angle, launch_angle_range
import numpy as np
import math

def test():
    alpha=0.25
    ve_v0=2.0
    tol_alpha=0.02
    phi_range=launch_angle_range(ve_v0,alpha,tol_alpha)
    print(" Max         Min")
    print(phi_range)

def negative_root():
    sin=launch_angle(3.0,2.0)
    print("expected: nan")
    print("actual: ",sin)

negative_root()
test()