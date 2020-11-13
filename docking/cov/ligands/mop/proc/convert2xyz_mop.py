import sys
import os
sys.path.append('/home/davialefe/docking/cov/')
import tools

files = os.listdir('/home/davialefe/docking/cov/ligands/mop/proc')
for file in files:
    if file.endswith('.arc'):
        tools.arc2xyz(file)