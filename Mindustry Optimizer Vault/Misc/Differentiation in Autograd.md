
Using requires_grad=True on parameters initiates a recording of every subsequent elementary mathematical operation. This chain of parameter-operator pairs forms the **computational graph**.

During the forward pass, input data flows through this chain of operations to produce a 'guess'. This guess is then compared to the ground truth using a **LOSS function**, which aggregates all the individual errors into a single scalar value.

Finally, .backward() is called on this error scalar. This triggers backpropagation, which travels backward through each individual parameter-operator pair (**in essence, differentiating through the entire graph**) to compute the **gradient** for each parameter.

This gradient represents the precise, relative influence ('blame') each parameter had on the total error. The optimizer then uses these gradients to update the parameters, adjusting the most influential ones more significantly.



*Map intuition to mathematical formulas for mathematical pass*
![[Screenshot 2025-07-18 at 10.45.39 PM.png]]