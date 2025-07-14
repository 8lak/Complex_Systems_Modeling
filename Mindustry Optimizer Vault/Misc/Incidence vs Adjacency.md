
###  **Adjacency Matrix (A)**

- **Dimensions:** n x n (node-by-node comparison).

- **Structure:** $A_{ij}$ = 1 if node i is connected to node j; 0 otherwise.

- **Undirected vs. Directed:** For undirected graphs, A is symmetric $A_{ij} = A_{ji})$. For directed graphs, A can be asymmetric $A_{ij} \neq A_{ji} = 1$.

- **Weighted:** Weights are easily represented: $A_{ij} = w_{ij}$.


###  **Incidence Matrix (S)**

- **Dimensions:** n x m (node-to-edge relationship).

- **Structure:** For an edge $e = (u, v)$, we set $S_{ue} = 1$ (tail) and $S_{ve} = -1$ (head). All other entries in column e are 0. This arbitrary signing is crucial.

- **Undirected vs. Directed:** The structure inherently captures orientation, making it behave similarly for both graph types.

- **Weighted:** Weights can be applied, often by multiplying the columns of S.