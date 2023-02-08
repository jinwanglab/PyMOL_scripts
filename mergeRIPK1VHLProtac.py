'''
How to merge warhead, linker, and ligand into one molecule?

Perquisite: chain ID: X-T2i, Y-VHL_ligand, Z-linker. NO HYDROGEN! (Current version of autoProtac will remove hydrogen at the beginning)

Since linker is variable, we need to delete overlapping atoms from the warhead and E3 ligand.
    T2i: N1-N4, C1-C6, C23-C24
    VHL: ?
Change all chain IDs into Z
Rename all residue IDs into PTC
Create CONECT at bridging atoms (need to nominate the bridging atom on the linker?)
Open with PyMOL and Export Molecule by PyMOL (so that atom name will be renamed)
'''

# Deprecated
# Use PyMOL API to do this

import os
import re


def alter(file, old_str, new_str):
    regex = re.compile(old_str)
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(regex, new_str, line))
    os.remove(file)
    os.rename("%s.bak" % file, file)


def delete(file, delete_str):
    regex = re.compile(delete_str)
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if regex.search(line):
                continue
            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)


# return atom ID for specific re search item.
def atomID(file, pattern):
    atom_list = []
    regex = re.compile(pattern)
    with open(file, "r", encoding="utf-8") as f1:
        for line in f1:
            if regex.search(line):
                atom_list.append(int(line[7:11]))
    return atom_list


# connect atoms
def create_CONECT(file, atom1, atom2):
    delete(file, "END")
    with open(file, "a", encoding="utf-8") as f1:
        f1.write("CONECT " + str(atom1) + " " + str(atom2))
        f1.write("\n" + "END")

os.chdir("C:\\Users\\Wang Lab\\Desktop")
os.chdir("C:\\Users\\19050\\Desktop")
# print(os.getcwd())

with open("mergetest.pdb", "r+", encoding='UTF-8') as pdb:
    pdb_line = pdb.readlines()

    chainX = [line for line in pdb_line if ' X' in line]
    chainY = [line for line in pdb_line if ' Y' in line]
    chainZ = [line for line in pdb_line if ' Z' in line]

    assert chainX != [], 'there is no chain X in pdb file. Have you nominated warhead molecule as chain X?'
    assert chainY != [], 'there is no chain Y in pdb file. Have you nominated E3 ligand as chain Y?'
    assert chainZ != [], 'there is no chain Z in pdb file. Have you nominated linker as chain Z?'

# Remove overlapping atoms in T2I warhead
delete("mergetest.pdb", 'C1 .....X')
delete("mergetest.pdb", 'C2 .....X')
delete("mergetest.pdb", 'C3 .....X')
delete("mergetest.pdb", 'C4 .....X')
delete("mergetest.pdb", 'C5 .....X')
delete("mergetest.pdb", 'C6 .....X')
delete("mergetest.pdb", 'C23.....X')
delete("mergetest.pdb", 'C24.....X')
delete("mergetest.pdb", 'N1 .....X')
delete("mergetest.pdb", 'N2 .....X')
delete("mergetest.pdb", 'N3 .....X')
delete("mergetest.pdb", 'N4 .....X')

# Remove overlapping atoms in VHL ligand
delete("mergetest.pdb", 'CA .....Y')
delete("mergetest.pdb", 'CB .....Y')
delete("mergetest.pdb", 'CG .....Y')
delete("mergetest.pdb", 'CD2.....Y')
delete("mergetest.pdb", 'N  .....Y')
delete("mergetest.pdb", 'OD1.....Y')
delete("mergetest.pdb", 'CAZ.....Y')
delete("mergetest.pdb", 'CBI.....Y')
delete("mergetest.pdb", 'CBG.....Y')
delete("mergetest.pdb", 'CAB.....Y')
delete("mergetest.pdb", 'CAC.....Y')
delete("mergetest.pdb", 'CAD.....Y')
delete("mergetest.pdb", 'NAV.....Y')
delete("mergetest.pdb", 'CAY.....Y')
delete("mergetest.pdb", 'OAF.....Y')
delete("mergetest.pdb", 'OAG.....Y')
delete("mergetest.pdb", 'CBJ.....Y')
delete("mergetest.pdb", 'FAI.....Y')
delete("mergetest.pdb", 'CAO.....Y')
delete("mergetest.pdb", 'CAP.....Y')

delete("mergetest.pdb", 'C14.....Z')

bridge_atom_VHL = atomID("mergetest.pdb", 'C   4YY')[0]
bridge_atom_linker = atomID("mergetest.pdb", 'C11 UNL')[0]
bridge_atom_T2I = atomID("mergetest.pdb", 'C7  UNK')[0]
bridge_atom_linker2 = atomID("mergetest.pdb", 'C4  UNL')[0]

create_CONECT("mergetest.pdb", bridge_atom_VHL, bridge_atom_linker)
create_CONECT("mergetest.pdb", bridge_atom_T2I, bridge_atom_linker2)

# unifying chain name
alter("mergetest.pdb", " X", " Z")
alter("mergetest.pdb", " Y", " Z")

# unifying residue name and res_id
alter("mergetest.pdb", "... Z....", "PTC Z   1")
