import os
import sys

sys.path.append('/home/davialefe/docking/cov/')

import tools

files = os.listdir('/home/davialefe/docking/cov/ligands/pdb')

for file in files:
    tools.pdb2xyz(file)