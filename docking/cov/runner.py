import os

#ligands = os.listdir('/home/davialefe/docking/cov/ligands/pdbqt_preparados')
configs = os.listdir('/home/davialefe/docking/cov/main_protease/configs')

receptor= 'main_protease_PDB_IC_6lu7.pdbqt'
ligand = '/home/davialefe/docking/cov/ligands/pdbqt_preparados/CN275.pdbqt'

#for ligand in ligands:
for config in configs:
    logname = config.replace('config','log')
    output = config.replace('config','output')
#ligandpath = f'/home/davialefe/docking/cov/ligands/pdbqt_preparados/{ligand}'
    configpath = f'/home/davialefe/docking/cov/main_protease/configs/{config}'
    cmd = f'vina --receptor {receptor} --ligand {ligand} --config {configpath} --log {logname}.txt --out {output}.pbdqt'
    os.system(cmd)