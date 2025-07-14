[[1.RL]]


Incremental Implementation

$$\begin{align*}  
Q_{k+1} &= \frac{1}{k} r_k + \frac{k-1}{k} Q_k \  
&= \frac{1}{k} r_k + \frac{k - 1}{k} Q_k \  
&= \frac{1}{k} r_k + \left(1 - \frac{1}{k}\right) Q_k \  
&= \frac{1}{k} r_k + Q_k - \frac{1}{k} Q_k \  
&= Q_k + \frac{1}{k} r_k - \frac{1}{k} Q_k \  
&= Q_k + \frac{1}{k} \left( r_k - Q_k \right)  
\end{align*}$$