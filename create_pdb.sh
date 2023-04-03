#!/bin/bash

for i in {1..25};
do
	head -$((i*37)) scan_points_optimized2.pdb | tail -36 > point$i
	# LEAVE 5 BLANK COLUMNS BEFORE THE COORDINATES TO GET THE PROPER SPACING IN .pdb FILE
	# SEE THE FILE scan_points_optimized.pdb 
       paste -d " " LEFT_PDB point$i	> point.pdb
       tleap -f tleap_f99.in
       tleap -f tleap_f14.in
       mkdir POINT$i
       mv point$i.* POINT$i
       done

