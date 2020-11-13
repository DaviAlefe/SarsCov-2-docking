import sys
import os
sys.path.append('/home/davialefe/docking/cov/')
import tools

files = os.listdir('/home/davialefe/docking/cov/ligands/mop/')
for file in files:
    if file.endswith('.mop'):
        cmd = f'/opt/mopac/MOPAC2016.exe {file}'
        print(cmd)
        os.system(cmd)
        cmd = f'mv {file[:-4]}.out ./proc'
        os.system(cmd)