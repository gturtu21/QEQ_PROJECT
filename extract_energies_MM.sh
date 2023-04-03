#!/bin/bash
touch energies
for i in {1..25}; do
	grep -A1 'NSTEP' POINT$i/min.out | head -2 | tail -1 >> energies
done

awk '{print $2}' energies > energies_MM

rm energies
