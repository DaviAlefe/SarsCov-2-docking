import os

files = os.listdir('/home/davialefe/docking/cov/ligands/mop/proc/xyz')

for file in files:
    if file.endswith('.xyz'):
        cmd = f'obabel {file} -O {file[:-4]}.pdb'
        os.system(cmd)
        cmd = f'mv {file[:-4]}.pdb  /home/davialefe/docking/cov/ligands/pdb_otimizados'
        os.system(cmd)