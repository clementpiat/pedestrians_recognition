"""
Test script that read the data
"""

import numpy as np
import pickle as pickle

f = open("data/data_acc_rot.dat","rb")
data = pickle.load(f,encoding="latin1")
f.close()

data_A = np.array(data[0])
data_B = np.array(data[1])
data_C = np.array(data[2])
label = np.array(data[3])

print(data_A.shape, label.shape)