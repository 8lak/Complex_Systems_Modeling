


## Cross entropy

"Cross-entropy loss measures the inefficiency of a predicted probability distribution in representing the true distribution. In classification, the 'true distribution' is treated as a one-hot vector where the correct class has a probability of 1.0. The loss is minimized when the model's predicted probability for the correct class approaches 1.0, effectively making the predicted distribution identical to the true distribution."

PyTorch's nn.CrossEntropyLoss efficiently combines a LogSoftmax and a NLLLoss to create a loss function that penalizes the model based on the log probability it assigns to the true class.

LogSoftmax = log(softmax(x)) turns the soft max values into logits which means higher values are closer to zero and smaller are farther away both both are less than zero. 

NLLLoss = basically just negates and chooses the probability for the true class.


