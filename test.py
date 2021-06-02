from pywigner import pywigner
import numpy as np

fact = np.zeros(101,dtype=np.float)
fact[0] = 1.
for i in range(1,101): fact[i] = fact[i-1] * np.float(i)

print(pywigner.wigner3j(2,6,4,0,0,0,fact))
print(pywigner.wigner3j(2,6,4,0,0,1,fact))
