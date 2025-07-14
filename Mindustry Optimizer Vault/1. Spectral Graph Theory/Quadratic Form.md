[[1.Spectral Graph Theory]]

The quadratic form is the engine that allows us to measure the "energy" of a signal on the graph.

**Formal Definition:** A function that maps a vector $x$ to a scalar via $x^T A x$.

 **The Pythagorean Intuition:** The simplest quadratic form uses the identity matrix, A = I.  

$x^TIx=x^Tx=x_{1}^2+x_{2}^2+⋯+x_{n}^2=∥x∥^2$

This is literally the **squared length** (or squared distance from the origin) of the vector x, which is the Pythagorean theorem in n-dimensions.

- **Generalization of x²:** A general quadratic form expands this idea. For a 2D vector x and matrix A, we get:  

$x^TAx=(x_1x_2)\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} =ax_1^2+(b+c)x_1x_2+dx_2^2​$

  
It generalizes the simple x² by including **cross-product terms** (x₁x₂), which represent interactions between the vector's components. It measures a "warped" or "stretched" distance, where the warping is defined by the matrix A.

Now consider the special case you stumbled upon, $(Ax)^T(Ax) = ||Ax||²$ This measures the **squared length of the transformed vector Ax**. It tells you how much the transformation A stretches or shrinks the vector x.