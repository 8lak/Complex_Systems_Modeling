[[1.Spectral Graph Theory]]


Basic facts about the spectrum 


fact1: the eigen values are bounded by 0 and 2 

**Intuition**: For the Normalized Laplacian all of the $\lambda_k$ are sure to fall between the bound. Why zero?
Since we know the Rayleigh Quotient uses the [[Quadratic Form]] we know it squares the equation its manipulating which simultaneously makes any value non-negative. As for two as an upper bounds this implies a maximum unstable frequency. And the maxmimum difference between two point on a signal would be -1 and +1 making it a movement of 2. 


fact2: connectivity and Spectral Gap

$\lambda_0$ is always zero since its the stable state. While $\lambda_1$ (Fiedler value) is always non zero ***if and only if the graph is connected***.  The number of zeros that appear is directly related to the number of connected components on the graph

**Intuition**: If the graph is disconnected then you can create a non-constant function that is equal to zero. Which disrupts the initial stable state you can solve or converge too. And also appears to be paradoxical that a non-constant or moving function can in fact have no energy. The only logical explanation would be that the function is a result of two separate entities that while constant themselves, global view misconstrues as a single moving object. 


Fact 3: Bipartiteness and Largest EigenValue $\lambda_{n-1}$ 

The Largest Eigenvalue is equal to 2 ***if and only if*** a connected component of the graph is bipartite [[Types of graphs]]. Such that one set of nodes has $f(v) = +c$ and another $f(v) = -c$
with all edges going between these two sets. This would maximize the difference in the numerator of the RQ.

Fact 4: Lower Bound on Fiedler Vector

- **The Concept:** The Fiedler value λ₁ can be bounded from below using the graph's diameter D (the longest shortest path between any two nodes) and its volume vol(G) (the sum of all degrees). Specifically, $λ₁ ≥ 1 / (D * vol G)$
    
- **The Intuition:** This connects the "spectral bottleneck" (λ₁) to a "physical bottleneck" (D). A graph with a very **large diameter** is "long and stringy," making it easy to cut in half. An easy-to-cut graph should have a **small λ₁**. The formula λ₁ ≥ 1 / (large number) correctly captures this inverse relationship. A small λ₁ implies a large diameter.

