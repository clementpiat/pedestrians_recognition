# Pedestrians Recognition

## Description. 
The goal of this is project to illustrate, on a toy example, the benefit of coordinate invariance
of persistent homology. The walks of 3 pedestrians A, B and C have been recorded using the accelerometer
sensors of smartphones carried in their pockets, leading to **3 multivariate time series in R3**
: each time series
represents the 3 coordinates of the acceleration of the corresponding pedestrian in a coordinate system
attached to the sensor. Since smartphones were carried in unknown different positions and were not fixed,
there is no correspondence between the coordinate systems of each smatphone, and thus these time series
cannot be compared using coordinates. Using a sliding window, each time series has been split in a list of
**100 times series made of 200 consecutive points**, that are stored in data A, data B and data C. To each set
of 200 points is associated a label A, B or C.
This project aims at doing supervised learning with persistence diagrams in order to achieve pedestrian
recognition.

## Tasks.
1. (Download the data together with a Python script to load it.)
2. Compute and save the 0-dimensional and 1-dimensional persistence diagrams of the Vietoris-Rips
filtrations built on top of each of the point clouds in R
3
.
3. Compute the matrix of pairwise bottleneck distances between diagrams and use a dimensionality
reduction algorithm to visualize them in 2D and 3D (using, e.g., Multidimensional Scaling).
4. Write a function to compute persistence landscapes. This function should take as input a persistence
diagram dgm (in the GUDHI format), a dimension k, the endpoints xmin, xmax of an interval, the
number nbnodes of nodes of a regular grid on the interval [xmin, xmax] and a number of landscapes
nbld, and output a nbld × nbnodes array storing the values of the first nbld landscapes of dgm on the
node of the grid. Check on some simple examples that your code is correct.
5. For each 0-dimensional and 1-dimensional persistence diagrams, compute the first 5 landscapes on a
relevant interval with a few hundred of nodes. Randomly split the data set with 80/20 train/test split,
and use a random forest to explore the performances of the 0-dimensional and 1-dimensional landscapes
to classify pedestrians. Compare the results you obtain using 0-dimensional landscapes, 1-dimensional
landscapes or both.
6. Do the same experiment, but this time use the raw data (3 × 200 array of acceleration coordinates).
Compare the obtained classification results to the previous one.

## Code. 

For the tasks 2 and 3, you can run the respective following scripts:
```
python compute_distance_matrix.py
```
```
python compute_persistence_diagrams.py
```
This will create the appropriate files in `./data/`.

The remaining tasks are covered directly in the notebook `./explore.ipynb`.
