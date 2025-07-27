
```python
# Neural Networks

# constructed with the torch.nn package. nn depends on autograd to define models and differntiate them

# nn.module contains laters and a method forward(input) that retursn the output
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
def __init__(self):
super().__init__()
# 1 input image channel, 6 output channels, 5x5 square convolution
# kernel
# nn.Conv2d(in_channels, out_channels, kernel_size)
self.conv1 = nn.Conv2d(1, 6, 5)
self.conv2 = nn.Conv2d(6, 16, 5)
# an affine operation: y = Wx + b
#nn.Linear(in_features, out_features)
self.fc1 = nn.Linear(16 * 5 * 5, 120) # 5*5 from image dimension
self.fc2 = nn.Linear(120, 84)
self.fc3 = nn.Linear(84, 10)

def forward(self, input):
#This entire first section is the "dimension reduction" and "clumping features that serve as a basis." It's a hierarchical process. Inital values are randomly created with processes like Kaiming He Initialization
#What it does: First convolutional layer.

#basis ->
c1 = F.relu(self.conv1(input))
# relu is added for learn non-linear relationships.
#F.relu(input):
#What it is: An Activation Function. It takes the output of a layer and applies the simple mathematical function max(0, x) to every single element. Any negative value becomes zero.

#What it does: First pooling layer.
# dimension reduce ->
s2 = F.max_pool2d(c1, (2, 2))
#F.max_pool2d(input, kernel_size):
#What it is: A Downsampling Layer. It slides a window (kernel_size, e.g., 2x2) over the input feature map and, for each window, keeps only the single maximum value.
#Why it's used:
#Dimensionality Reduction: It makes the feature maps smaller (e.g., a 14x14 map becomes 7x7), which reduces the number of parameters and computations in later layers.
#Local Invariance:#
# structure basis ->
c3 = F.relu(self.conv2(s2))
#dimension reduce ->
s4 = F.max_pool2d(c3, 2)
#flatten (global space) ->
s4 = torch.flatten(s4, 1)
#torch.flatten(input, 1):
#What it is: A Reshaping Operation. It takes a multi-dimensional tensor and collapses it into a 1D vector.
# Why it's used: It is the critical bridge between the convolutional world and the linear world.
#basis of global space using given structure basis ->
f5 = F.relu(self.fc1(s4))
f6 = F.relu(self.fc2(f5))
#final projection or final basis
output = self.fc3(f6)
return output

net = Net()

print(net)
```




```

# The Core Process of Training a Neural Network in PyTorch # ----------------------------------------------- # CONCEPT: The Setup # ------------------------------ #
A Neural Network is a collection of nested functions (Layers). These layers # contain learnable parameters (weights and biases) stored in Tensors. # torch.autograd is the engine that tracks all operations on these tensors, # building a computational graph to enable automatic differentiation. 

# ------------------------------ # CONCEPT: The Training Loop (The Unbreakable 5-Step Sequence) # This entire process is performed for every single batch of data. 

Also known as Stochastic Gradient Descent (SGD)


# ----------------------------------------------------------------------------- # Step 1: Zero the Gradients # ACTION: optimizer.zero_grad() # WHY: Erase the gradients from the previous batch. Gradients accumulate by # default, so we reset them at the start of each new training step. 

# Step 2: Forward Propagation # ACTION: output = model(input) # WHY: The model makes its best guess. The input data flows through the # network's functions, producing a raw output. This is the "guess." 

# Step 3: Compute Loss # ACTION: loss = loss_function(output, target) # WHY: Compare the "guess" to the "truth" (the target labels). The loss # function computes a single scalar value representing the total error. This # scalar is the starting point for backpropagation. 

# Step 4: Backward Propagation # ACTION: loss.backward() # WHY: Calculate the gradients. Autograd traverses the computational graph # backward from the loss, computing the gradient of the loss with respect to # every learnable parameter (d_loss/d_parameter). This is the "blame attribution." 

# Step 5: Update Weights (Optimization) # ACTION: optimizer.step() # WHY: Adjust the parameters. The optimizer uses the gradients computed in the # previous step to update the model's weights (e.g., using the rule: # weight = weight - learning_rate * gradient). This is the "nudge" that # should make the model perform better on the next iteration.
```

## attempt to build from scratch refinements 

```python

def test(dataloader, model, loss_fn): # .setup ... 
model.eval() test_loss, correct = 0, 0 with torch.no_grad(): # This is the key addition 
for X, y in dataloader: 
X, y = X.to(device), y.to(device) 
pred = model(X) 
test_loss += loss_fn(pred, y).item() 
correct += (pred.argmax(1) == y).type(torch.float).sum().item() 
# ... the rest of your code ... 
with torch.no_grad():` tells PyTorch, "For everything indented under me, do not track gradients. Just do the math." This is a crucial optimization for inference.
#### 3. No Optimizer, No `backward()` You correctly identified that a test loop doesn't involve `optimizer.zero_grad()`, `loss.backward()`, or `optimizer.step()`. This is because we are only *measuring*, not *learning*. 

#### 4. The Metrics: Accuracy and Loss This is the heart of the test loop. 
 `test_loss += loss_fn(pred, y).item()` * **`.item()` 
#is important:
#** The `loss` is a tensor with a `grad_fn`. `.item()` extracts the raw Python number from it, detaching it from the graph and preventing memory pile-ups. 

#* You correctly sum up the loss from each batch. 
#* `correct += (pred.argmax(1) == y).type(torch.float).sum().item()` 

#* Let's break this brilliant line down: 
#1. **`pred.argmax(1)`:** 
#For each image in the batch, this finds the **index** of the highest score. This is the model's predicted class. 

#2. **`== y`:
#** This compares the vector of predicted indices to the vector of true labels (`y`). The result is a boolean tensor, e.g., `[True, False, True, True]`. 

#3. **`.type(torch.float)`:** Converts the booleans to floats: `[1.0, 0.0, 1.0, 1.0]`. 

#4. **`.sum()`:** Adds them up to get the total number of correct predictions in the batch (in this case, `3.0`). 

#5. **`.item()`:** Extracts that number as a Python float.


#**Your Final Assessment is Perfect** Yes, you need to do this a few more times. But you are not just "going through the motions." You have successfully written down the correct structure. The next step is to rebuild it from a blank script a few times. With each attempt, one more piece (`model.eval()`, `with torch.no_grad()`, `argmax(1)`) will move from "syntax I had to look up" to "a tool I understand." This is the final stage of the learning process.
```
