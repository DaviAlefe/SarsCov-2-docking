import sys
import os
sys.path.append('/home/davialefe/docking/cov/')
import tools

files = os.listdir('/home/davialefe/docking/cov/ligands/xyz')
for file in files:
    if file.endswith('.xyz'):
        tools.xyz2mop(file)