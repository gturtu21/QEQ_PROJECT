#!/usr/bin/python3

class qeq_parameters():
    def __init__(self, PARAMS_TYPE, ATOM_LIST, AMINOACID_NAME, NUMBER_OF_ATOMS):
        self.param_type = PARAMS_TYPE
        self.atoms = ATOM_LIST
        self.aminoacid = AMINOACID_NAME
        self.natoms = NUMBER_OF_ATOMS
        self.filename = f"parameters_{self.param_type}.qeq"
        if self.param_type == 'M2011':
            self.params = {'H':(3.7248, 19.2186, 0.8203),
                           'C':(4.9218, 12.0000, 0.6387),
                           'O':(8.5000, 16.6240, 1.0898),
                           'N':(6.4603, 14.0634, 1.0000)}
        elif self.param_type == 'M2015':
            self.params = {'H':(3.7248,  19.2186,  0.8203),
                           'C':(5.2323,  12.0000,  0.7028),
                           'O':(8.5000,  16.6244,  1.0898),
                           'N':(6.0111,  13.4074,  1.0000)}
        elif self.param_type == 'T2018':
            self.params = {'H':(4.7133,  14.1880, 0.8034),
                           'C':(5.5984,  12.0468,  0.6343),
                           'O':(7.0639,  14.5122,  0.8939),
                           'N':(7.1787,  15.2106,  0.9571)}

        elif self.param_type == 'D2020':
            self.params = {'H':(3.5442,  18.7696,  0.7390),
                           'C':(4.4087,  14.1202,  0.5516),
                           'O':(8.5000,  16.9566,  1.1000),
                           'N':(6.6335,  14.2946,  1.0000)}

    def write_param_file(self):
        with open(self.filename, 'w') as f:
            for index, atom in enumerate(self.atoms):
                chi = self.params[atom][0]
                eta = self.params[atom][1]
                gamma = self.params[atom][2]
                line = f"{index+1}    {chi:8.4f}  {eta:8.4f}  {gamma:8.4f} \n"
                f.write(line)
        return
    def write_input_lammps(self, scaling = False):
        if scaling:
            SPECIAL_BONDS = "special_bonds lj  0.0 0.0 0.5 coul  0.0 0.0 0.25"
            input_lammps = f"input_{self.param_type}_scaling.in"
        else:
            SPECIAL_BONDS = "special_bonds amber"
            input_lammps = f"input_{self.param_type}.in"
        to_print = f"""units    real
neighbor	1.3 bin
neigh_modify    every 1 delay 0 check yes once no page 500000 one 50000
atom_style	full
bond_style      harmonic
angle_style     harmonic
dihedral_style  harmonic
pair_style      lj/cut/coul/long 12.0
pair_modify     mix arithmetic
kspace_style    pppm 1e-4
read_data       data.{self.aminoacid}_ff14
{SPECIAL_BONDS}
######################################
### OUTPUT OPTIONS
thermo          1000
thermo_style    multi
######################################
group		{self.aminoacid} id 1:{self.natoms}
fix             QEQFIX all qeq/reax 1 0.0 10.0 1.0e-6  {self.filename} maxiter 500
compute         charge{self.aminoacid} {self.aminoacid} property/atom q
dump            charges{self.aminoacid} {self.aminoacid} custom 1000 charges_{self.aminoacid}_{self.param_type}.txt id c_charge{self.aminoacid}
dump_modify 	charges{self.aminoacid} sort id
######### MINIMIZE
dump 		dumpmin all custom 1 min.lammpstrj id mol type x y z ix iy iz 
minimize 	1.0e-4 1.0e-6 1000 5000 """
        with open(input_lammps, 'w') as f:
            f.write(to_print)
        return
    def write_input_lammps_reaxff(self):
        atoms_string = '  '.join(self.atoms)
        input_lammps = f"input_{self.param_type}_reaxff.in"
        to_print = f"""units        real
neighbor	1.3 bin
atom_style	charge
pair_style      reaxff NULL
read_data       data.{self.aminoacid}_reaxff
pair_coeff	* * {self.param_type}.reax  {atoms_string}
######################################
### OUTPUT OPTIONS
thermo          1000
thermo_style    multi
######################################
group		{self.aminoacid} id 1:{self.natoms}
fix             QEQFIX all qeq/reaxff 1 0.0 10.0 1.0e-6 reaxff
compute         charge{self.aminoacid} {self.aminoacid} property/atom q
dump            charges{self.aminoacid} {self.aminoacid} custom 1 charges_{self.aminoacid}.txt id c_charge{self.aminoacid}
dump_modify 	charges{self.aminoacid} sort id
######### MINIMIZE
minimize 	1.0e-4 1.0e-6 1000 5000 """

        with open(input_lammps, 'w') as f:
            f.write(to_print)
        return
