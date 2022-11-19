"""
this is my libary for computation that require the
manipulation of complex numbers
"""

import math

#z1+z2
def complexAdd(complex_1, complex_2):
    return([complex_1[0]+complex_2[0],complex_1[1]+complex_2[1]])

#z1-z2
def complexMin(complex_1, complex_2):
    return([complex_1[0]-complex_2[0],complex_1[1]-complex_2[1]])

#z1/z2
def complexDiv(complex_1, complex_2):
    x = pow(complex_2[0],2) + pow(complex_2[1],2)
    a = complex_1[0]*complex_2[0] + complex_1[1]*complex_2[1]
    b = complex_1[1]*complex_2[0] - complex_1[0]*complex_2[1]
    return([a/x,b/x])

def complex_inRasein():
    pass

z1 = [1,3]
z2 = [1,1]

output = complexDiv(z1,z2)

print(output)