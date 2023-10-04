from range import launch_angle, launch_angle_range, arcsin
import numpy as np
import math

def test():
    print("Testing range of angles given alpha=0.25, ve_v0=2.0, tol_alpha=0.02")
    alpha=0.25
    ve_v0=2.0
    tol_alpha=0.02
    phi_range=launch_angle_range(ve_v0,alpha,tol_alpha)
    print(" Max         Min")
    print(phi_range)

def arcsin_test():
    print("Testing arcsin function with 0.5")
    asin=arcsin(0.5)
    print("expected: 0.5235987755982988")
    print("actual:  ", asin)

def negative_root():
    print("Testing what happens if there is a negative value under the root")
    sin=launch_angle(3.0,2.0)
    print("expected: nan")
    print("actual: ",sin)

negative_root()
test()
arcsin_test()