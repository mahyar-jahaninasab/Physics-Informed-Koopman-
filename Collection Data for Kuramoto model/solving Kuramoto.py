import numpy as np
import scipy.linalg as spla
import scipy.fftpack as fp
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
import networkx as nx



np.random.seed(2)

## Parameters

N = 16 #number of oscilators

rho = np.random.uniform(0, 5)


dt = 0.001
sim_time = 0.2
n_it = int(sim_time / dt)
## Init vals

w_nat = np.random.randn(N) #natural frequencey



thetas = np.zeros((N, n_it))
thetas_dot = np.zeros_like(thetas)
time_vals = np.linspace(0., sim_time, n_it)


w_i =  2 * np.pi * np.random.rand(N)

# Adjacency matrix

def initialize_network(n):
    G = nx.random_geometric_graph(n, radius=1)
    A = nx.adjacency_matrix(G).toarray()
    return A
adj_mat = initialize_network(N)
theta = w_i
for ittt in range(n_it):
    # sum of sins
    theta_mat = np.repeat(theta.reshape(N, 1), N, axis=1)
    diffs = theta_mat.T - theta_mat #self adjoint mat
    sins = np.sin(diffs)
    sins = adj_mat * sins
    sums_sins = np.sum(sins, axis=1)
    theta_new = theta + dt * (w_nat + rho * sums_sins)
    thetas[:, ittt] = theta
    thetas_dot[:, ittt] = np.divide(theta_new - theta, dt)
    theta = theta_new
Snapshots.append(thetas_dot)

