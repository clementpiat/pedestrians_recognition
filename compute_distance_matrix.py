import gudhi as gd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle
from sklearn.manifold import MDS

def get_pairwise_bottleneck_distance_matrix(persistence_diagrams):
    distance_matrix = np.zeros((300,300))
    for i, pd1 in enumerate(tqdm(persistence_diagrams)):
        for j, pd2 in enumerate(persistence_diagrams[i+1:], i+1):
            
            distance_matrix[i,j] = distance_matrix[j,i] = gd.bottleneck_distance(pd1,pd2)
    
    return distance_matrix

def visualize_distance_matrix(distance_matrix, filename):
    mds = MDS(n_components=2, dissimilarity='precomputed')
    projection = mds.fit_transform(distance_matrix)

    plt.scatter(projection[:,0], projection[:,1], c=[0]*100+[1]*100+[2]*100)
    plt.savefig(f"data/{filename}")

def main():
    """
    We need to run this with a big value of max_length so that in all the persistence diagrams we have only one point at the infinity
    Otherwise we have infinite distances between some diagrams and we can't compute MDS
    """
    max_edge_length = "10.0"
    f = open(f"data/persistence_diagrams_{max_edge_length}.dat","rb")
    data = pickle.load(f)
    f.close()

    distance_matrix_0, distance_matrix_1 = list(map(get_pairwise_bottleneck_distance_matrix, data))

    visualize_distance_matrix(distance_matrix_0, f"distance_matrix_0_{max_edge_length}.jpg")
    visualize_distance_matrix(distance_matrix_1, f"distance_matrix_1_{max_edge_length}.jpg")


if __name__ == "__main__":
    main()