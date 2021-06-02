
import numpy as np
from .codes import wigner_code

__all__ = ['wigner3d']

def wigner3j(j1,j2,j3,m1,m2,m3,fact):
    args = j1*2,j2*2,j3*2,m1*2,m2*2,m3*2
    val = wigner_code._w3js(*args,fact)
    #val =  wigner_code._w3js(int(1),int(2),int(3),int(1),int(2),int(3),fact)
    return val
