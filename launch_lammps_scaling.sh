#!/bin/bash
LAMMPS_PATH="/home/giorgio/bin/lammps-22Dec22/tools/amber2lmp"
for i in {1..25};
do
       cp input_*.in POINT$i
       cp param*qeq POINT$i
       cd POINT$i
       lmp_mpi -i input_M2011_scaling.in -screen MONTI2011.out
       lmp_mpi -i input_M2015_scaling.in -screen MONTI2015.out
       lmp_mpi -i input_T2018_scaling.in -screen TRNKA2018.out
       lmp_mpi -i input_D2020_scaling.in -screen DUIN2020.out
       cd ..
       done

