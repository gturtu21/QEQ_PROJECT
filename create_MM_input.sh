#!/bin/bash

aminoacid='GLY'

## GENERATE "tleap_f14.in" file
cat << END > tleap_f14.in

source leaprc.protein.ff14SB
${aminoacid} = loadpdb point.pdb
savepdb ${aminoacid} ${aminoacid}.pdb

set $aminoacid box {30.0 30.0 30.0} 
saveamberparm ${aminoacid} ${aminoacid}_ff14.top    ${aminoacid}_ff14.crd
saveamberparm ${aminoacid} ${aminoacid}_ff14.prmtop ${aminoacid}_ff14.rst7
quit

END

cat << END > vmd_create_reaxff_data.sh
package require topotools
topo readlammpsdata data.${aminoacid}_ff14
topo writelammpsdata data.${aminoacid}_reaxff charge
quit
END

cat << END > launch_min.sh
#!/bin/bash

for i in {1..25}; do
	cp min.in POINT\$i
	cd POINT\$i
	sander -O -i min.in -o min.out -p ${aminoacid}_ff14.prmtop -c ${aminoacid}_ff14.rst7 &	
	cd ..
done

END

chmod +x launch_min.sh

rm -r POINT*
natoms=$(head -1 optimized_geom.xyz)
awk '{print substr($0,1,26)}' ${aminoacid}.pdb > LEFT_PDB
awk '{print substr($0,28,78)}' optimized_geometries.pdb > RIGHT_PDB



echo $natoms
for i in {1..25};
do
       head -$((i*(natoms+1))) RIGHT_PDB | tail -$((natoms)) > point$i
       paste -d " " LEFT_PDB point$i > point.pdb
       rm point$i
       mkdir POINT$i
       cp point.pdb POINT$i/
       cp tleap_f14.in POINT$i/
       cp vmd_create_reaxff_data.sh  POINT$i/
       cd POINT$i
       tleap -f tleap_f14.in
       cp point.*pdb point$i.pdb
       python /usr/local/lammps/tools/amber2lmp/amber2lammps.py ${aminoacid}_ff14
       vmd -dispdev text -e vmd_create_reaxff_data.sh
       cd ..
done

ntype=$(grep "atom types" POINT1/data."$aminoacid"_ff14 | awk '{print $1}')
grep -A $((ntype+1)) "Masses" POINT1/data."$aminoacid"_ff14 | awk '{print $2}' | tail -$ntype >  atom_masses.txt

