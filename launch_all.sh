#!/bin/bash

cd MM
./launch_min.sh &
cd ..
cd QEQ_LAMMPS
./launch_lammps.sh &
cd ..
cd QEQ_LAMMPS_WITH_SCALING
./launch_lammps_scaling.sh &
cd ..
cd REAXFF
./launch_lammps_reax.sh &
