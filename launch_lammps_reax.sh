#!/bin/bash
LAMMPS_PATH="/home/giorgio/bin/lammps-22Dec22/tools/amber2lmp"
for i in {1..25};
do
       cp input_*reax*.in POINT$i
       cp *.reax POINT$i
       cd POINT$i
       lmp_mpi -i input_M2011_reaxff.in -screen MONTI2011.out
       lmp_mpi -i input_M2015_reaxff.in  -screen MONTI2015.out
       lmp_mpi -i input_T2018_reaxff.in  -screen TRNKA2018.out
       lmp_mpi -i input_D2020_reaxff.in -screen DUIN2020.out
       cd ..
       done

