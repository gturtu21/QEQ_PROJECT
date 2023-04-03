#!/bin/bash
touch energies_MM
for i in {1..24}; do
	grep -A1 'NSTEP' POINT$i/min.out | head -2 | tail -1 | awk '{print $2}' >> energies_MM
done

