import numpy as np
import pickle as pickle

def read_data():
    f = open("data/data_acc_rot.dat","rb")
    data = pickle.load(f,encoding="latin1")
    f.close()

    data_A = np.array(data[0])
    data_B = np.array(data[1])
    data_C = np.array(data[2])
    label = np.array(data[3])

    return(data_A, data_B, data_C, label)