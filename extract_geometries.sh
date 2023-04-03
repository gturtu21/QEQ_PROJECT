#!/bin/bash
gaussianlog=$1
grep -B 400 "Optimized Parameters" $gaussianlog > just_optimized.txt


grep -A 35  "      1          1           0" just_optimized.txt | awk '{print $2}'  > atom_columns.txt
grep -A 35  "      1          1           0" just_optimized.txt | awk '{print $4, $5, $6}'  > scan_points_optimized2.txt




sed -i 's/1/h/g' atom_columns.txt
sed -i 's/6/c/g' atom_columns.txt
sed -i 's/7/n/g' atom_columns.txt
sed -i 's/8/o/g' atom_columns.txt



paste atom_columns.txt scan_points_optimized2.txt > scan_points_optimized2.xyz 
