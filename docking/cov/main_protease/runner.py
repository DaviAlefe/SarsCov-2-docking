import os

#ligands = os.listdir('/home/davialefe/docking/cov/ligands/pdbqt_preparados')
ligands = ['CN394.pdbqt', 'CN275.pdbqt','CN395.pdbqt']
configs = os.listdir('/home/davialefe/docking/cov/main_protease/configs')

receptor= 'main_protease_PDB_IC_6lu7.pdbqt'
#ligand = '/home/davialefe/docking/cov/ligands/pdbqt_preparados/CN275.pdbqt'

for ligand in ligands:
    if ligand.endswith('.pdbqt'):
        ligandpath = f'/home/davialefe/docking/cov/ligands/pdbqt_preparados/{ligand}'
        cmd = f'mkdir {ligand[:-6]}'
        os.system(cmd)
        for config in configs:
            logname = config.replace('config','log')
            if logname in checkpoint_CN338:
                continue
            output = config.replace('config','output')
            configpath = f'/home/davialefe/docking/cov/main_protease/configs/{config}'
            cmd = f'vina --receptor {receptor} --ligand {ligandpath} --config {configpath} --log {logname}.txt --out {output}.pbdqt'
            os.system(cmd)

            #move output files to ligand's directory
            mv = f'mv {logname}.txt ./{ligand[:-6]}'
            os.system(mv)
            mv = f'mv {output}.pbdqt ./{ligand[:-6]}'
            os.system(mv)