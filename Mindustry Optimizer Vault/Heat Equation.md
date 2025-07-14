(the opposing force to equilibrium convergence in a diffusion system)

Heat Equation 

![[Screenshot 2025-06-21 at 1.40.00 AM.png]]
**Intuition** : So as we apply a laplacian to a node signal we get the net flows which act as change per node which can be considered the ,Convergence to Equilibrium, modeled by the heat equation. Which just relates that the time derivative of a node potential is proportional to the negative laplacian of the current node potential. Which makes sense because the current $Lf$ would give us the current rate of changes or time derivatives with respect to $f$. 

**Formalization** : **The Intuition:**  
The rate of change of heat at a node $\frac{df_u}{dt}$  is proportional to the difference between its neighbors' heat and its own heat. If a node is hotter than its neighbors, it loses heat $\frac{df_u}{dt} < 0$. If it's colder, it gains heat $\frac{df_u}{dt} > 0$. The negative sign in $−L$ ensures heat flows from hot to cold. (Negative is applied since hotter would be positive values and cold negative so its counteracts the "direction")


Two methods to compute 

spectral method which is just exponentiating the laplacian decomposing it and applying the basis to the initial vector and then to the exponentiated eigen matrix.

Or iterative approach where we simply use the mechanism of matrices approaching largest eigen value and since it negated to simulate transfer it reaches eigen value 0 which is the largest of a negated matrix.