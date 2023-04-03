#!/usr/bin/python3
import os
from parameters_class_qeq import qeq_parameters
AMINOACID = 'GLY'
NUMBER_OF_ATOMS = 19

with open('atom_list', 'r') as fo:
    ATOM_LIST = fo.readlines()[0].split()
print(ATOM_LIST)
#ATOM_LIST = ["H", "C", "C", "O", "N", "H", "H"]


PARAMS = ["M2011", "M2015", "T2018", "D2020"]
for p in PARAMS:
    param_class = qeq_parameters(p, ATOM_LIST, AMINOACID, NUMBER_OF_ATOMS)
    param_class.write_input_lammps()
    param_class.write_input_lammps(scaling=True)
    param_class.write_input_lammps_reaxff()
    param_class.write_param_file()

