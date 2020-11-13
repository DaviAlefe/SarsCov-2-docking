import os

receptor= 'main_protease_PDB_IC_6lu7.pdbqt'
ligand = '/home/davialefe/docking/cov/ligands/pdbqt_preparados/CN338.pdbqt'

configs = os.listdir('/home/davialefe/docking/cov/main_protease/configs')


checkpoint_CN338 = ['log-main_protease_PDB_IC_6lu7-CN275-[-26.294,-17.397,118.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,-17.397,28.953000000000003].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,-17.397,58.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,-17.397,88.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,12.603,118.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,12.603,28.953000000000003].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,12.603,58.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,12.603,88.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,42.603,118.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,42.603,28.953000000000003].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,42.603,58.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,42.603,88.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,72.603,118.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,72.603,28.953000000000003].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,72.603,58.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-26.294,72.603,88.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-56.294,-17.397,118.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-56.294,-17.397,28.953000000000003].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-56.294,-17.397,58.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-56.294,-17.397,88.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-56.294,12.603,118.953].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-56.294,12.603,28.953000000000003].txt.txt',
 'log-main_protease_PDB_IC_6lu7-CN275-[-56.294,12.603,58.953].txt.txt']

for config in configs:
    logname = config.replace('config','log')
    if logname in checkpoint_CN338:
        continue
    output = config.replace('config','output')
    configpath = f'/home/davialefe/docking/cov/main_protease/configs/{config}'
    cmd = f'vina --receptor {receptor} --ligand {ligand} --config {configpath} --log {logname}.txt --out {output}.pbdqt'
    os.system(cmd)

    #move output files to ligand's directory
    mv = f'mv {logname}.txt ./CN338'
    os.system(mv)
    mv = f'mv {output}.pbdqt ./CN338'
    os.system(mv)