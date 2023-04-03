#!/usr/bin/python3
import numpy as np

atom_masses = np.loadtxt("atom_masses.txt")

with open("atom_list",'w') as fo :
    for a in atom_masses:
        if int(a) == 1:
            fo.write('H ')
        elif int(a) == 12:
            fo.write('C ')
        elif int(a) == 14:
            fo.write('N ')
        elif int(a) == 16:
            fo.write('O ')

