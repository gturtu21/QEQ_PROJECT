#!/bin/bash

for i in {1..25}; do
	cp min.in POINT$i
	cd POINT$i
	sander -O -i min.in -o min.out -p GLY_ff14.prmtop -c GLY_ff14.rst7 &	
	cd ..
done

