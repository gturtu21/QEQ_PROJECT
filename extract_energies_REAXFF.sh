#!/bin/bash
rm energies_*
for i in {1..25}; do

	grep 'TotEng' POINT$i/MONTI2011.out | head -1 | awk '{print $3}' >> energies_LAMMPSQEQ_MONTI2011

	grep 'TotEng' POINT$i/MONTI2015.out | head -1 | awk '{print $3}' >> energies_LAMMPSQEQ_MONTI2015

	grep 'TotEng' POINT$i/TRNKA2018.out | head -1 | awk '{print $3}' >> energies_LAMMPSQEQ_TRNKA2018
	grep 'TotEng' POINT$i/DUIN2020.out | head -1 | awk '{print $3}' >> energies_LAMMPSQEQ_DUIN2020
done

