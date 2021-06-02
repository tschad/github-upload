## cython file that does link between C and python

from numpy cimport ndarray as ar
from numpy import linspace, empty
cimport numpy as np

cdef extern:
  void c_w3js(int* j1,int* j2,int* j3,int* m1,int* m2,int* m3,double* fact,double* w3j_val)

def _w3js(int j1,int j2,int j3,int m1,int m2,int m3,np.ndarray fact):
  cdef double w3j_val
  c_w3js(&j1, &j2, &j3, &m1, &m2, &m3,<double*> fact.data, &w3j_val)
  return w3j_val
