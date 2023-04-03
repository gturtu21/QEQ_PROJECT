#!/usr/bin/python3
import sys
sys.path.append("/home/PERSONALE/giorgio.turtu2/mylibrary")
from myfunctions import set_plot_style
import numpy as np
import matplotlib.pyplot as plt

set_plot_style()


SCALING=True

QM_HF = np.loadtxt("QM/energies_HF.txt", skiprows = 4)
MM_AMBER = np.loadtxt("MM/energies_MM")
if SCALING:
    PATH_QEQ_LAMMPS="QEQ_LAMMPS_WITH_SCALING"
else:
    PATH_QEQ_LAMMPS="QEQ_LAMMPS"
MM_LAMMPS_MONTI = np.loadtxt(f"{PATH_QEQ_LAMMPS}/energies_LAMMPSQEQ_MONTI2015")
MM_LAMMPS_MONTI2011 = np.loadtxt(f"{PATH_QEQ_LAMMPS}/energies_LAMMPSQEQ_MONTI2011")
MM_LAMMPS_TRNKA2018 = np.loadtxt(f"{PATH_QEQ_LAMMPS}/energies_LAMMPSQEQ_TRNKA2018")
MM_LAMMPS_DUIN2020 = np.loadtxt(f"{PATH_QEQ_LAMMPS}/energies_LAMMPSQEQ_DUIN2020")
REAXFF_MONTI2011 = np.loadtxt("REAXFF/energies_LAMMPSQEQ_MONTI2011")
REAXFF_MONTI2015 = np.loadtxt("REAXFF/energies_LAMMPSQEQ_MONTI2015")
REAXFF_TRNKA2018 = np.loadtxt("REAXFF/energies_LAMMPSQEQ_TRNKA2018")
REAXFF_DUIN2020 = np.loadtxt("REAXFF/energies_LAMMPSQEQ_DUIN2020")
#ANGLES = QM_HF[:,0]


ANGLES = np.arange(-180, 195, 15)


ENE_HF = (QM_HF[:,1] - QM_HF[0,1]) * 627.5
ENE_AMBER = MM_AMBER[:] - MM_AMBER[0]
ENE_LAMMPS_MONTI = (MM_LAMMPS_MONTI[:] - MM_LAMMPS_MONTI[0])
ENE_LAMMPS_MONTI2011 = (MM_LAMMPS_MONTI2011[:] - MM_LAMMPS_MONTI2011[0])
ENE_LAMMPS_TRNKA2018 = (MM_LAMMPS_TRNKA2018[:] - MM_LAMMPS_TRNKA2018[0])
ENE_LAMMPS_DUIN2020 = (MM_LAMMPS_DUIN2020[:] - MM_LAMMPS_DUIN2020[0])
ENE_REAXFF11 = (REAXFF_MONTI2011[:] - REAXFF_MONTI2011[0])
ENE_REAXFF15 = (REAXFF_MONTI2015[:] - REAXFF_MONTI2015[0])
ENE_REAXFF18 = (REAXFF_TRNKA2018[:] - REAXFF_TRNKA2018[0])
ENE_REAXFF20 = (REAXFF_DUIN2020[:] - REAXFF_DUIN2020[0])
## PLOT AMBER+QEQ vs QM
#plt.plot(ANGLES, ENE_AM1[:], label = 'AM1')
fig, ax = plt.subplots(1,1)

ax.plot(ANGLES, ENE_HF[:], '-o', color = 'k', label = 'HF/6-31g*')
## NO QEQ
ax.plot(ANGLES[:], ENE_AMBER, '-o', color = 'b', label = 'AMBER-ff14SB')

## WITH QEQ
ax.plot(ANGLES[:], ENE_LAMMPS_MONTI, '-v', color = 'r', label =      'Qeq(Monti2015)')
ax.plot(ANGLES[:], ENE_LAMMPS_MONTI2011,  '-+', color = 'r', label = 'Qeq(Monti2011)')
ax.plot(ANGLES[:], ENE_LAMMPS_TRNKA2018,  '-*', color = 'r', label = 'Qeq(Trnka2018)')
ax.plot(ANGLES[:], ENE_LAMMPS_DUIN2020,  '-p', color = 'r', label = 'Qeq(Duin2020)')

ax.set_xlabel('Angle (degrees)')
ax.set_ylabel(r'$\Delta$E (kcal mol$^{-1}$)')
ax.set_ylim([-10,25])
#plt.legend(ncol = 2)
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
#          ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
if SCALING:
    plt.savefig("GLY_scan_PSI_comparison_AMBERQEQ_SCALING.svg")
else:
    plt.savefig("GLY_scan_PSI_comparison_AMBERQEQ.svg")
plt.show()



## PLOT REAXFF vs QM
plt.plot(ANGLES, ENE_HF[:], '-o', color = 'k', label = 'HF/6-31g*')
## NO QEQ
plt.plot(ANGLES[:], ENE_AMBER, '-o', color = 'b', label = 'AMBER-ff14SB')

# WITH REAXFF

plt.plot(ANGLES[:], ENE_REAXFF11,  '-+', color = 'g', label = 'REAXFF11')
plt.plot(ANGLES[:], ENE_REAXFF15,  '-v', color = 'g', label = 'REAXFF15')
plt.plot(ANGLES[:], ENE_REAXFF18,  '-*', color = 'g', label = 'REAXFF18')
plt.plot(ANGLES[:], ENE_REAXFF20,  '-p', color = 'g', label = 'REAXFF20')
plt.xlabel('Angle (degrees)')
plt.ylabel(r'$\Delta$E (kcal mol$^{-1}$)')

plt.ylim([-10,25])
#plt.legend(ncol=2)
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
#          ncol=2, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig("GLY_scan_PSI_comparison_REAXFF.svg")
plt.show()


from sklearn.metrics import mean_squared_error
print("MONTI2011", mean_squared_error(ENE_HF, ENE_LAMMPS_MONTI2011))
print("MONTI2015", mean_squared_error(ENE_HF, ENE_LAMMPS_MONTI))
print("T2018", mean_squared_error(ENE_HF, ENE_LAMMPS_TRNKA2018))
print("D2020", mean_squared_error(ENE_HF, ENE_LAMMPS_DUIN2020))
