[[1.Spectral Graph Theory]]

The Rayleigh Quotient uses the quadratic form of the Laplacian to assign a single score to a signal, representing its smoothness or frequency. See [[Signal Decomposition on Graphs via Incidence Matrices]] for the underlying mechanics of the Laplacian and the usage of divergence and gradient to find variance. 


$R(f)=\frac{f^T L f}{f^T f}=\frac{\sum_{(u,v)\in E}(f(u)-f(v))^2}{\sum_{v\in V}f(v)^2}$

- **Vector Notation:** All forms of the Rayleigh Quotient are ratios of inner products. The **inner product**, $\langle f, g \rangle = \sum_x f(x)\,g(x)$, is the formal tool for converting vector relationships (like alignment and length) into scalars.

### 1.  **The Unnormalized Rayleigh Quotient**
$R(f)=\frac{\langle f,Lf\rangle}{\langle f,f\rangle}=\frac{f^T L f}{f^T f}=\frac{\sum_{(u,v)\in E}(f(u)-f(v))^2}{\sum_{v\in V}f(v)^2}$
- **Interpretation:** Total Signal Variance / Total Signal Intensity. Treats all nodes equally.
### 2. **The Normalized Rayleigh Quotient**
$R_{\mathrm{norm}}(f)=\frac{\langle f,Lf\rangle}{\langle f,Df\rangle}=\frac{f^T L f}{f^T D f}=\frac{\sum_{(u,v)\in E}(f(u)-f(v))^2}{\sum_{v\in V}d_v\,f(v)^2}$

- **Interpretation:** Total Signal Variance / **Degree-Weighted** Signal Intensity. Gives more importance to nodes with high degrees (hubs). This is often more meaningful for real-world networks.

Types of RQs

1. **The "Variance" Denominator $Σ(f(v) - f̄)²dᵥ)$:**
    
    - This form is inherently **constrained**. The centering operation $(f(v) - f̄)$ implicitly builds in the orthogonality condition needed to find a specific eigenvalue like $λ₁$. The f̄ term is calculated from the function f itself, so this denominator is always relative to the function's own internal structure.
        
2. **The "Magnitude" Denominator $Σf(v)²dᵥ$:**
    
    - This form is **universal and unconstrained**. It measures the function's magnitude against a fixed, absolute baseline of zero. It doesn't know or care if the function f is centered or an eigenvector.
        
    - Because it is not tied to any particular constraint or property of f, it is the **only one** that can be used to prove a **universal law** like $λₖ ≤ 2$, which must hold true for all possible functions, not just the special ones that happen to be eigenvectors.

#### **Extracting the Eigenvalue: The Quotient's Purpose**

The Rayleigh Quotient is a machine designed to reveal eigenvalues.

- **The Eigenvector Property:** For an eigenvector f of a matrix L, we have the defining relationship $Lf = λf$, where λ is the scalar eigenvalue.
    
- **The "Extraction" Process:** If we feed an eigenvector f into the (unnormalized) Rayleigh quotient:  

    $R(f)=\frac{\langle f,Lf\rangle}{\langle f,f\rangle}$
      
    We can substitute $Lf$ with $λf$:  
$=\frac{\langle f,Lf\rangle}{\langle f,f\rangle}=\frac{\langle f,λf\rangle}{\langle f,f\rangle}=λ\frac{\langle f,f\rangle}{\langle f,f\rangle}=λ$
    
- **Conclusion:** The Rayleigh quotient isolates the scaling factor λ. It directly tells us the "frequency" (the eigenvalue) of the specific pattern we fed it (the eigenvector).



### Geometric Breakdown of RQ

##### **The Numerator:$fᵀ A f$ (The Dot Product that Measures Alignment)**

- **Intuition:** "the alignment comes from the multiplication and since f is a vector and Af becomes a vector it becomes a dot product"
    
- **Formalization:** This is 100% correct.$f^T A f$ is precisely the dot product (inner product) between the original vector f and the transformed vector Af. The geometric formula for the dot product is:  
$⟨f,Af⟩=∥f∥∥Af∥cos⁡(θ)$

#####  **The Denominator:$fᵀ f$ (The Normalizer that Enables Comparison)**

- **Your Intuition:** "the division of the f^2"
    
- **Formalization:** The denominator is 
-$f^Tf=∥f∥_2$
     the squared length of the original vector. Its job is **normalization**. It ensures that the value of the Rayleigh Quotient depends only on the direction of f, not its length. This is crucial for comparing the "smoothness" of different patterns regardless of their overall signal strength.
![[Screenshot 2025-06-08 at 10.36.40 PM.png]]
**The Quadratic Form ($f^T L f$):** When you form the Rayleigh quotient, the numerator is the quadratic form of the Laplacian.

![[Screenshot 2025-06-21 at 1.20.39 AM.png]]    


**Interpretation:** This is the **squared length of the gradient of f**. The Rayleigh quotient, is essentially asking: "How large is the gradient of f, relative to the size of f itself?"
    
- **Conclusion:** The Rayleigh quotient is a measure of how much a signal f "lives" in the gradient space. Signals with small Rayleigh quotients have small gradients; they are smooth. Eigenvectors of L are the special signals whose gradients are perfectly scaled versions of themselves (after accounting for the divergence step).

![[Screenshot 2025-06-21 at 1.20.44 AM.png]]