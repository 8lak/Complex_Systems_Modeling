[[1.Spectral Graph Theory]]


Laplacian matrices can be used to tell us the connectivity between nodes. More specifically the number of zero eigen values tell you the number of connected components. Its eigen vectors become a basis for the frequencies or vibration pattern. Its eigen values are the scalar applied to it. 




## Initial Intuition
Laplacian is defined as L = D - A there exist other nuanced versions but for now I will use the most basic one. The laplacian tell us the similarity between nodes. ( you have a summation between different values at node i from neighbors the specific values Lf I'm not sure if derived from the graph across a column or row. but I understand that it tells us the relative difference of a node. We can relate laplacian eigenpairs to PCA eigen pairs where they tell the principal axes of difference. However, PCA tells us the variance on static data and Laplacian eigen pairs tell us the variance between nodes. **Intuition** f we imagine a given set of nodes as a finite subspace we can define height as frequency and can then determine convergence from the differing heights across the space. This contour emerges from the values of the matrix and hence why we can retrieve its spectral properties. More specifically we consider the eigen vectors to be the unit basis frequencies or the pattern of connectivity between nodes. The eigen values tell us how smooth to rough a frequency is. I like to think its similar to how stable a frequency is. We can directly relate this to markov chains and probabilities since by defining a finite space we are already in a markov scenario that allows us to explore the probabilities of the states. I'm a still trying to discern the exact difference between the probability states we get from a transitional matrix vs the interpretation of the eigen pairs of a random walk laplacian but I suppose it would be measuring the probabilities differences across states like the transitional space between states if that makes sense(i have to refine this section) **intuition** We can think of it like removing the anchor of a normal distribution and just looking at the variance or spread. 

$D = degree matrix$
$A = adjacency matrix$
#### Unnormalized Laplacian 
**When degree weights aren't a concern. Regular graph**
$L = D - A$

#### Normalized  Laplacian
**Degree balancing symmetric spectral properties for general graphs**
$\mathcal{L} = I - D^{-1/2}A D^{-1/2}$
View [[Diagonalization]] for scaling intuition


The form for a particular node this would be the formula for a particular entry which signifies the  scaled difference summed over the $d_u$ neighbors scaled by the root of our current node's degree.
$\displaystyle \mathcal L\,g(u) = \frac{1}{\sqrt{d_u}}\sum_{v\sim u}\Bigl(\frac{g(u)}{\sqrt{d_u}} - \frac{g(v)}{\sqrt{d_v}}\Bigr)$

For a k-regular graph
$\displaystyle \mathcal L = I - \frac{1}{k}\,A$

This is just the matrix form where we expand $L$ to $D - A$ and simplify. For General graphs
$\displaystyle \mathcal L = T^{-1/2}\,L\,T^{-1/2} = I - T^{-1/2}\,A\,T^{-1/2}$

where  $D=\mathrm{diag}(d_1,\dots,d_n)$ and $T=D^{-1/2}$.

Essentially telling us the overall difference between all nodes and their respective neighbors scaled by its degrees rooted.

#### Random Walk Laplacian
When working with random-walk dynamics and markov chains interpretations
$L_{\mathrm{rw}} = I - D^{-1}A$
