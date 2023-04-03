#!/usr/bin/python3
import sys

def print_lines_from_to(file_input, file_output, i1, ATOMS_LIST):
    NATOMS = len(ATOMS_LIST)
    with open(file_input) as fhand:
        lines = fhand.readlines()[i1+3:i1+NATOMS+3]
    for l,a in zip(lines, ATOMS_LIST):
        _, _, _, x, y, z = l.split()
        print(a, x, y, z, file = file_output)

def get_atom_num(file_input):
    with open(file_input) as fhand:
        lines = fhand.readlines()
        for i, l in enumerate(lines):
            if 'Distance matrix (angstroms):' in lines[i+2]:
                NATOM = l.split()[0]
                return int(NATOM)
def get_atom_list(file_input, number_of_atoms):
    atom_list = []
    with open(file_input) as fhand:
        lines = fhand.readlines()
        for i, l in enumerate(lines):
            if 'Charge =  0 Multiplicity = 1' in l:
                li = i
                atom_lines = lines[li+1:li+number_of_atoms+1]
            else:
                pass
        for l in atom_lines:
            atom_list.append(l.split()[0].lower())
    return atom_list
gaussian_log = sys.argv[1]
#atom_names = sys.argv[2]
natoms = get_atom_num(gaussian_log)
atom_list = get_atom_list(gaussian_log, natoms)
print(len(atom_list))
line_numbers = []
line_types = []   ## type 1 is "Center     Atomic      Atomic             Coordinates (Angstroms)"
                  ## type 2 is "Optimized Parameters"
with open(gaussian_log) as f:
    for i, l in enumerate(f.readlines()):
        if "Center     Atomic      Atomic             Coordinates (Angstroms)" in l:
            line_numbers.append(i)
            line_types.append(1)
        elif "Optimized Parameters" in l:
            line_numbers.append(i)
            line_types.append(2)
    print("###")
    #print(line_numbers)
    #print(line_types)

c = 0
for i, t in enumerate(line_types):
    output = open(f"optimized_geom.xyz", "a")
    try:
        if line_types[i+1] == 2:
            print(natoms, file = output)
            print("", file = output)
            print_lines_from_to(gaussian_log, output, line_numbers[i], atom_list)
            #print("", file = output)
            c += 1
    except IndexError:
        print('TOTAL POINTS EXTRACTED:', c)

    output.close()
