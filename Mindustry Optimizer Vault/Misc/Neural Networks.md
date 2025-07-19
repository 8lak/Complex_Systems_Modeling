![[Screenshot 2025-07-18 at 10.52.28 PM.png]]

Simple feed-forward network takes input and pushes it through layers until an output is received

Usual procedure:
- Define Neural Network with some learnable parameters
- Iterate over datasets of inputs
- Process input through network
- Compute loss 
- Propagate gradients back into network's parameters
- update weights with a simple update rule $weight = weight - learning\_rate * gradient$
- 