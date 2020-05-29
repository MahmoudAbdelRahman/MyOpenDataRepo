#Principal component Analysis

import numpy as np
from sklearn.decomposition import PCA

from scipy.io import loadmat
import json


import matplotlib.pyplot as plt

alld =[]
def pap(n):
    if n == 0:
        alld.append(0)
        return 0
    else:
        d =  n + pap(n-1)
        alld.append(d)
        return d


print(pap(50))
print(alld)

plt.plot(alld)
plt.show()
# matFile = loadmat('./DataSets/CVRR_dataset_trajectory_clustering/cross.mat')
# tracks = matFile["tracks"]

# print(tracks[0][0])

# # X = np.array()
# pca = PCA(n_components=9)
# pca.fit(tracks[0][0].tolist())


# print(pca.explained_variance_ratio_)  

# print(pca.singular_values_)  