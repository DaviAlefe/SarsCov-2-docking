def pdb2xyz(filein):
  if filein.endswith('.pdb'):
    name = filein[:-4]
  cmd = f'obabel {name}.pdb -O ../xyz/{name}.xyz'
  from os import system
  return system(cmd)

def xyz2mop(filein):
  file = open(filein, 'r')
  lines = file.readlines()
  text = [' AUX LARGE CHARGE=0 SINGLET  PM6  OPT PRECISE PRTXYZ\n']
  text.append(lines[1])
  text.append(lines[0])
  for line in lines[2:]:
    line = line.split()
    line = ['    '+line[0], line[1], '1', line[2], '1', line[3], '1']
    line = '       '.join(line)
    text.append(line+'\n')
  text = ''.join(text)
  file.close()
  file = open(f'../mop/{filein[:-4]}.mop', 'wt')
  file.write(text)
  file.close()

def arc2xyz(filein):
  with open(filein,'r') as file:
    lines = file.readlines()
    for line in lines:
      if 'FINAL GEOMETRY OBTAINED' in line:
        i = lines.index(line)
    mop = lines[i+1:]
    xyz = lines[i+2:]
    xyz[0] = lines[i+3]
    xyz[1] = lines[i+2]
    for i in range(len(xyz)):
      xyz[i] = xyz[i].replace('+1',' ')
    xyz = ''.join(xyz)
    mop = ''.join(mop)
    mopOut = open(f'./mop/{filein[:-4]}.mop', 'w')
    mopOut.write(mop)
    mopOut.close()
    xyzOut = open(f'./xyz/{filein[:-4]}.xyz', 'w')
    xyzOut.write(xyz)
    xyzOut.close()

def make_centers(spacing, center, npoints):
  import numpy as np
  len = spacing * npoints
  ngrids = np.ceil(len/30).astype(int)
  centers = []
  for i in range(-np.ceil(ngrids[0]/2).astype(int),np.ceil(ngrids[0]/2).astype(int)+1):
    for j in range(-np.ceil(ngrids[1]/2).astype(int)+1,np.ceil(ngrids[1]/2).astype(int)+1):
      for k in range(-np.ceil(ngrids[2]/2).astype(int)+1,np.ceil(ngrids[2]/2).astype(int)+1):
        centerN = [center[0]+i*30, center[1]+j*30, center[2]+k*30]
        centers.append(centerN)
  return centers

def chg_param(filename, param, param_value):
    infile = open(filename, 'rt')
    text = infile.readlines()
    i = 0
    for line in text:
        if param in line:
            i = text.index(line)
            line_i = text[i].split()
            line_i[2] = str(param_value)
            text[i] = ''.join(line_i) + '\n'
    text = ''.join(text)
    infile.close()
    infile = open(filename, 'wt')
    infile.write(text)
    infile.close()

def make_config(receptor, ligand,center):
  #copiar o arquivo
  with open('/home/davialefe/docking/config_model.txt', 'r') as file:
    text = file.read()
    new_name = f'config-{receptor}-{ligand}-[{center[0]},{center[1]},{center[2]}].txt'
    out = open(new_name, 'w')
    out.write(text)
    out.close()
  #alterar os parâmetros da cópia
  chg_param(new_name, 'receptor',receptor)
  chg_param(new_name, 'ligand',ligand)
  chg_param(new_name, 'center_x', center[0])
  chg_param(new_name, 'center_y', center[1])
  chg_param(new_name, 'center_z', center[2])

def extract_affinity(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if '--+--' in line:
        i = lines.index(line)
        data = lines[i+1]
        data = data.split()
        affinity = float(data[1])
  return affinity

def extract_affinities(file):
  import numpy as np
  affinities = []
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if '--+--' in line:
        i = lines.index(line)
        for j in range(i+1,i+10):
          data = lines[j]
          data = data.split()
          affinity = float(data[1])
          affinities.append(affinity)
  return np.array(affinities)

def extract_all(file):
  import numpy as np
  data = []
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if '--+--' in line:
        i = lines.index(line)
        for j in range(i+1,i+10):
          data_j = lines[j]
          data_j = data_j.split()[1:]
          data.append(data_j)
  return np.array(data).astype(float)


def make_heatmap(array,fileout,directory):
  import seaborn as sns
  import numpy as np
  import matplotlib.pyplot as plt

  fig, (ax0, ax1, ax2) = plt.subplots(1,3, figsize = (18,6))
  sns.heatmap(array[0], annot=True, ax=ax0, cbar=False)
  sns.heatmap(array[1], annot=True, ax=ax1, cbar=False)
  sns.heatmap(array[2], annot=True, ax=ax2, cbar=False)

  fig.savefig(f'{directory}/{fileout}.png')

def similarity(a,b):
  #retorna similaridade entre dois numpy arrays de qualquer ordem.
  # 0 é nada similar, 1 é muito similar
  # Os arrays são normalizados, então a similaridade não leva em conta os módulos das entradas, mas sim o ângulo no espaço dimensional dos arrays

  import tensorflow as tf
  s = tf.losses.CosineSimilarity()
  cs = s(a,b)
  return -1*cs.numpy()

def make_similarity_matrix(directory, protein, outdir):
  #directory: location of the tensors (they should be the only files on the directory)
  #protein's name (ex: 'main_protease')
  #outdir : directory where the csv and png will be saved
  tensors = os.listdir(directory)

  import numpy as np
  similarity_matrix = np.ones((len(tensors),len(tensors)))

  for i in range(len(tensors)):
    for j in range(len(tensors)):
      if j<i:
        a = np.load(f'{directory}/{tensors[i]}')
        b = np.load(f'{directory}/{tensors[j]}')
        similarity_matrix[i][j] = similarity(a,b)
      if j>=i:
        similarity_matrix[i][j]=None

  import pandas as pd
  df = pd.DataFrame(similarity_matrix,index=[tensor[:-4] for tensor in tensors],columns=[tensor[:-4] for tensor in tensors])
  df.to_csv(f'{outdir}/{protein}.csv')

  import seaborn as sns
  mask = np.triu(df)
  fig, ax = plt.subplots(1,1, figsize=(24,18))
  sns.heatmap(df, mask=mask, annot=True,fmt='.3g', ax=ax)
  ax.set_title(f'{protein} Similarity Matrix')
  fig.savefig(f'{outdir}/{protein}.png')