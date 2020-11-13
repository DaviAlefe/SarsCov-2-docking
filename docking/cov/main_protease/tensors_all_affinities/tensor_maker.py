import numpy as np
import sys
sys.path.append('/home/davialefe/docking/cov/')
import tools
import os

centers = np.array([[-56.294, -17.397, 28.953000000000003], [-56.294, -17.397, 58.953], [-56.294, -17.397, 88.953], [-56.294, -17.397, 118.953], [-56.294, 12.603, 28.953000000000003], [-56.294, 12.603, 58.953], [-56.294, 12.603, 88.953], [-56.294, 12.603, 118.953], [-56.294, 42.603, 28.953000000000003], [-56.294, 42.603, 58.953], [-56.294, 42.603, 88.953], [-56.294, 42.603, 118.953], [-56.294, 72.603, 28.953000000000003], [-56.294, 72.603, 58.953], [-56.294, 72.603, 88.953], [-56.294, 72.603, 118.953], [-26.294, -17.397, 28.953000000000003], [-26.294, -17.397, 58.953], [-26.294, -17.397, 88.953], [-26.294, -17.397, 118.953], [-26.294, 12.603, 28.953000000000003], [-26.294, 12.603, 58.953], [-26.294, 12.603, 88.953], [-26.294, 12.603, 118.953], [-26.294, 42.603, 28.953000000000003], [-26.294, 42.603, 58.953], [-26.294, 42.603, 88.953], [-26.294, 42.603, 118.953], [-26.294, 72.603, 28.953000000000003], [-26.294, 72.603, 58.953], [-26.294, 72.603, 88.953], [-26.294, 72.603, 118.953], [3.7059999999999995, -17.397, 28.953000000000003], [3.7059999999999995, -17.397, 58.953], [3.7059999999999995, -17.397, 88.953], [3.7059999999999995, -17.397, 118.953], [3.7059999999999995, 12.603, 28.953000000000003], [3.7059999999999995, 12.603, 58.953], [3.7059999999999995, 12.603, 88.953], [3.7059999999999995, 12.603, 118.953], [3.7059999999999995, 42.603, 28.953000000000003], [3.7059999999999995, 42.603, 58.953], [3.7059999999999995, 42.603, 88.953], [3.7059999999999995, 42.603, 118.953], [3.7059999999999995, 72.603, 28.953000000000003], [3.7059999999999995, 72.603, 58.953], [3.7059999999999995, 72.603, 88.953], [3.7059999999999995, 72.603, 118.953]])
x = np.array([center[0] for center in centers])
y = np.array([center[1] for center in centers])
z = np.array([center[2] for center in centers])

#unique values of centers for mapping to the tensor
x = sorted(np.unique(x))
y = sorted(np.unique(y))
z = sorted(np.unique(z))

tensor = np.ones((len(x),len(y),len(z),9))

directories = os.listdir('/home/davialefe/docking/cov/main_protease')[:27]
for item in directories:
    directory = os.listdir(f'/home/davialefe/docking/cov/main_protease/{item}')
    for file in directory:
        if file.startswith('log-'):
            path = f'/home/davialefe/docking/cov/main_protease/{item}/{file}'
            energies = tools.extract_affinities(path)

            start = file.index('[') + 1
            end = file.index(']')
            file_center = np.array(file[start:end].split(',')).astype(float)
            e_position = np.array([np.where(x==file_center[0])[0][0], np.where(y==file_center[1])[0][0], np.where(z==file_center[2])[0][0]])
            tensor[tuple(e_position)] = energies
        np.save(f'/home/davialefe/docking/cov/main_protease/tensors_all_affinities/{item}',tensor)