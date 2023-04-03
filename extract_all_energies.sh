#!/bin/bash

cd MM
./extract_energies_MM.sh &
cd ..
cd QEQ_LAMMPS
./extract_energies_QEQ_LAMMPS.sh &
cd ..
cd QEQ_LAMMPS_WITH_SCALING
./extract_energies_QEQ_LAMMPS.sh &
cd ..
cd REAXFF
./extract_energies_REAXFF.sh &
