import numpy as np
import pickle as pickle
import gudhi as gd
import argparse
import json
from tqdm import tqdm

from utils import read_data

"""
Simply compute and store persistent diagrams for each time serie.
Corresponds to Task 2.
"""

def main(args):
    data_A, data_B, data_C, _ = read_data()
    persistence_diagrams = ([],[])
    for data in [data_A, data_B, data_C]:
        for time_serie in tqdm(data):
            skeleton = gd.RipsComplex(points=time_serie, max_edge_length=args.max_edge_length)
            simplex_tree = skeleton.create_simplex_tree(max_dimension=2)

            simplex_tree.persistence()
            rips_barcodes_0 = simplex_tree.persistence_intervals_in_dimension(0)
            rips_barcodes_1 = simplex_tree.persistence_intervals_in_dimension(1)

            persistence_diagrams[0].append(rips_barcodes_0)
            persistence_diagrams[1].append(rips_barcodes_1)


    print("\nSaving result...")
    with open(f"data/persistence_diagrams_{args.max_edge_length}.dat", "wb") as f:
        pickle.dump(persistence_diagrams, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--max_edge_length", type=float, default=10.0, help="Max edge length for the Vietoris-Rips filtration")
                        
    args = parser.parse_args()
    print(f"> args:\n{json.dumps(vars(args), sort_keys=True, indent=4)}\n")
    main(args)