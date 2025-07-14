# graph representation and basic SGT engine
# Phase 1 Goal Get a basic system where an RL agen can modify edge weights of a fixed graph, 
# and success is measured by changes in the spectral properties
import numpy as np
#import networkx as nx

# Essentials
# Represt a graph as a matrix
# Finding its degree matrix from the adjacency matrix
# Construct the Laplacian matrix


np.random.randn(5)

#A list of lists is a generic Python structure you can use to organize data in rows and columns.
graph = [[0, 5, 2, 0],
            [5, 0, 1, 6],
               [2, 1, 0, 3],
               [0, 6, 3, 0]]


#A NumPy array is a specialized, memory-efficient, and computationally powerful (vectorized operations) object designed for numerical work, which can be created from a list of lists but is fundamentally different under the hood.

adjmatrix = np.array(graph)

def degree_matrix(adjmatrix):
    # Calculate the degree matrix from the adjacency matrix

    # sums values across columns, 2 for across rows
    degrees = np.sum(adjmatrix, axis=1)
    # we could also create a 1s vector np.ones(4,1) and multiply the adjacency matrix by it and then use np.diag
    # but this is more efficient
    return np.diag(degrees)

degree = degree_matrix(adjmatrix)

def laplacian_matrix(adjmatrix):
    # Calculate the Laplacian matrix from the adjacency matrix
    # L = D - A
    D = degree_matrix(adjmatrix)
    return D - adjmatrix

laplacian = laplacian_matrix(adjmatrix)

def normalized_laplacian_matrix(adjmatrix):
    # Calculate the normalized Laplacian matrix
    # L_norm = I - D^(-1/2) * A * D^(-1/2)
    D = degree_matrix(adjmatrix)
    D_inv_sqrt = np.diag(1.0 / np.sqrt(np.diag(D)))
    return np.eye(len(adjmatrix)) - D_inv_sqrt @ adjmatrix @ D_inv_sqrt

def spectral_properties(laplacian):
    # Calculate the eigenvalues and eigenvectors of the Laplacian matrix
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
    return eigenvalues, eigenvectors



# Retrieving the first two eigenvalues and their corresponding eigenvectors tells us two twhings: The multiplicity of the zero eigenvalue indicates the number of connected components in the graph,
# and the second one also known as the Fiedler value, indicates the connectivity of the graph. The higher the value, the more connected the graph is, the smaller the value, the more disconnected the graph is or has a bottleneck.
#print(f"These are the first two eigen values representing the connected components and the Fiedler value: \n{eigenvalues[0:2]}")
#print(f"These are the eigenvectors of aforementioned eigenvalues: \n{eigenvectors[:, 0:2]}")





# --- Helper function to print graph info (optional but useful) ---
def print_graph_info(name, adj_matrix):
    print(f"\n--- {name} ---")
    print("Adjacency Matrix:")
    print(adj_matrix)
    laplacian = laplacian_matrix(adj_matrix)
    eigenvalues, eigenvectors = spectral_properties(laplacian)
    print("Laplacian Matrix:")
    print(laplacian)
    print("Eigenvalues:", eigenvalues[0:2])
    print(f"Fiedler Vector: \n{eigenvectors[:, 0:2]}")  # Assuming eigenvalues sorted
    print("-" * (len(name) + 8))

# --- 1. Path Graph (P4: 4 nodes, 3 edges) ---
# 0 -- 1 -- 2 -- 3
adj_P4 = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
])
# print_graph_info("Path Graph P4", adj_P4)

# --- 2. Cycle Graph (C4: 4 nodes, 4 edges) ---
# 0 -- 1
# |    |
# 3 -- 2
adj_C4 = np.array([
    [0, 1, 0, 1],  # Node 0 connected to 1 and 3
    [1, 0, 1, 0],  # Node 1 connected to 0 and 2
    [0, 1, 0, 1],  # Node 2 connected to 1 and 3
    [1, 0, 1, 0]   # Node 3 connected to 0 and 2
])
# print_graph_info("Cycle Graph C4", adj_C4)

# --- 3. Complete Graph (K4: 4 nodes, 6 edges) ---
# All nodes connected to all other nodes
adj_K4 = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
])
# print_graph_info("Complete Graph K4", adj_K4)

# --- 4. Star Graph (S3+center: 1 center (node 0) + 3 peripheral (nodes 1,2,3)) ---
#   1
#   |
# 0 -- 2
#   |
#   3
adj_S3_center = np.array([
    [0, 1, 1, 1],  # Node 0 (center) connected to 1, 2, 3
    [1, 0, 0, 0],  # Node 1 connected to 0
    [1, 0, 0, 0],  # Node 2 connected to 0
    [1, 0, 0, 0]   # Node 3 connected to 0
])
# print_graph_info("Star Graph S3 (center=0)", adj_S3_center)

# --- 5. Disconnected Graph (Two C3s: 6 nodes) ---
# Triangle 1: 0 -- 1 -- 2 -- 0
# Triangle 2: 3 -- 4 -- 5 -- 3
adj_Disconnected_2_C3s = np.array([
    [0, 1, 1, 0, 0, 0],  # Triangle 1
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],  # Triangle 2
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
])
# print_graph_info("Disconnected Graph (2 C3s)", adj_Disconnected_2_C3s)

# --- 6. "Bridge" Graph (Two K3s connected by one edge) ---
# K3_A: nodes 0, 1, 2
# K3_B: nodes 3, 4, 5
# Bridge: edge between node 0 (from K3_A) and node 3 (from K3_B)
adj_Bridge_K3_K3 = np.array([
    [0, 1, 1, 1, 0, 0],  # Node 0 (K3_A) connected to 1, 2 (K3_A) and 3 (bridge)
    [1, 0, 1, 0, 0, 0],  # Node 1 (K3_A)
    [1, 1, 0, 0, 0, 0],  # Node 2 (K3_A)
    [1, 0, 0, 0, 1, 1],  # Node 3 (K3_B) connected to 0 (bridge) and 4, 5 (K3_B)
    [0, 0, 0, 1, 0, 1],  # Node 4 (K3_B)
    [0, 0, 0, 1, 1, 0]   # Node 5 (K3_B)
])
# print_graph_info("Bridge Graph (K3-K3)", adj_Bridge_K3_K3)

# --- 7. Barbell Graph (Two K3s connected by a P2 path) ---
# K3_A (0,1,2) --- Path_Node (3) --- K3_B (4,5,6)
# Edge: (2,3) and (3,4)
adj_Barbell_K3_P_K3 = np.array([
    # K3_A (nodes 0, 1, 2)
    [0, 1, 1, 0, 0, 0, 0], #0
    [1, 0, 1, 0, 0, 0, 0], #1
    [1, 1, 0, 1, 0, 0, 0], #2 (connects to path node 3)
    # Path_Node (node 3)
    [0, 0, 1, 0, 1, 0, 0], #3 (connects to 2 and 4)
    # K3_B (nodes 4, 5, 6)
    [0, 0, 0, 1, 0, 1, 1], #4 (connects to path node 3)
    [0, 0, 0, 0, 1, 0, 1], #5
    [0, 0, 0, 0, 1, 1, 0]  #6
])
# print_graph_info("Barbell Graph K3-P-K3", adj_Barbell_K3_P_K3)

list_of_graphs = [
    ("Path Graph P4", adj_P4),
    ("Cycle Graph C4", adj_C4),
    ("Complete Graph K4", adj_K4),
    ("Star Graph S3 (center=0)", adj_S3_center),
    ("Disconnected Graph (2 C3s)", adj_Disconnected_2_C3s),
    ("Bridge Graph (K3-K3)", adj_Bridge_K3_K3),
    ("Barbell Graph K3-P-K3", adj_Barbell_K3_P_K3)
]

for name, adj_matrix in list_of_graphs:
    print_graph_info(name, adj_matrix)
    
# The above code defines a set of graphs and calculates their spectral properties, including the Laplacian matrix and eigenvalues.
# This is useful for understanding the connectivity and structure of the graphs, which can be applied in various fields such as network analysis, machine learning, and graph theory.