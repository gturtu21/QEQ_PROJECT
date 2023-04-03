#!/bin/bash
rm -r ../MM
rm -r ../QEQ_LAMMPS
rm -r ../QEQ_LAMMPS_WITH_SCALING
rm -r ../REAXFF
rm optimized_geom.xyz

#./extract_geometries.py trp_scan_diedro_HF.log atom_columns.txt
./extract_geometries.py gly_scan_diedro_HF.log 
vmd -dispdev text -e vmd_convert_to_pdb.sh optimized_geom.xyz
./create_MM_input.sh  &> /dev/null &
./create_atom_list.py 
./write_parameters_file.py 

sleep	10

#try:
mkdir ../MM
mkdir ../QEQ_LAMMPS
mkdir ../QEQ_LAMMPS_WITH_SCALING
mkdir ../REAXFF

## CREATE NECESSARY DIRS
cp -r POINT* ../MM/
cp -r POINT* ../QEQ_LAMMPS/
cp -r POINT* ../QEQ_LAMMPS_WITH_SCALING/
cp -r POINT* ../REAXFF/

# FOR PURE MM
cp  launch_min.sh ../MM/
cp  min.in ../MM
cp  extract_energies_MM.sh ../MM
# FOR QEQ
cp  parameters_*.qeq ../QEQ_LAMMPS/
cp  input_*.in ../QEQ_LAMMPS/
cp  extract_energies_QEQ_LAMMPS.sh ../QEQ_LAMMPS
cp  launch_lammps.sh ../QEQ_LAMMPS
# FOR QEQ + SCALING
cp parameters_*qeq ../QEQ_LAMMPS_WITH_SCALING/
cp input_*scaling.in ../QEQ_LAMMPS_WITH_SCALING/
cp extract_energies_QEQ_LAMMPS.sh ../QEQ_LAMMPS_WITH_SCALING/
cp launch_lammps_scaling.sh ../QEQ_LAMMPS_WITH_SCALING/
# FOR REAX
cp *reax ../REAXFF/
cp input_*reax*.in ../REAXFF/
cp extract_energies_REAXFF.sh ../REAXFF/
cp launch_lammps_reax.sh ../REAXFF/

