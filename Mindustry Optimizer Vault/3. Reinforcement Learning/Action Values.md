[[1.RL]]


As an overview, we can understand simple reinforcement learning agents as having two primary aspects: a **learning mechanism** and an **action-selection mechanism**. The learning mechanism is responsible for tracking the value or desirability of actions, effectively creating the agent's internal representation of the world. The action-selection mechanism then transforms this internal representation into "movement," or a concrete decision on how to act.

Action Value methods:
Stationary 

1. Sample Average 1/k weighted difference
Non-Stationary
 - recency-weighted average 1/c weighted difference
- 

Action Selection:
1. Soft max Selection: soft max which is a the way to make the probabilities between actions more accentuated and making it relative so its out of 1 and transformed from negative numbers
2. Greedy
3. Epsilon Greedy
4. Optimistic Greedy

Incremental Implementation

$$\begin{align*}  
Q_{k+1} &= \frac{1}{k} r_k + \frac{k-1}{k} Q_k \  
&= \frac{1}{k} r_k + \frac{k - 1}{k} Q_k \  
&= \frac{1}{k} r_k + \left(1 - \frac{1}{k}\right) Q_k \  
&= \frac{1}{k} r_k + Q_k - \frac{1}{k} Q_k \  
&= Q_k + \frac{1}{k} r_k - \frac{1}{k} Q_k \  
&= Q_k + \frac{1}{k} \left( r_k - Q_k \right)  
\end{align*}$$

2.7 Optimistic Initial Value: Basically instead of setting to zero we start with a reward that is greater than possible reward across all actions which gives an initial state of high exploration and as the action is picked more times the true value is converged to and exploitation begins. Effective for stationary problems. 


2.8 Reinforcement comparison:
Reinforcement Comparison introduces a novel agent architecture. Its core component is a "rolling indicator," the **reference reward (r_bar)**, which serves as a baseline to judge whether a new reward is better or worse than the agent's recent average experience. This r_bar is typically a recency-weighted average of all rewards the agent has received.

The learning rule in RC is unique: it does not learn or store long-term action-values (Q(a)). Instead, an individual reward is used only momentarily to update a **preference** for the action taken. The preference update, p(a) ← p(a) + α(R - r_bar), is structurally similar to a traditional value update, but it operates on preferences relative to the global r_bar baseline. This creates a sort of hierarchy where actions are judged not on their absolute merit, but on their performance relative to the agent's overall average. These learned preferences are then fed into a softmax function to produce a policy from which the next action is selected.


2.9 Pursuit method:

In contrast, the Pursuit Method can be concisely described as a more dynamic greedy approach. It uses a conventional learning rule to update its estimates of long-term action-values, Q(a).

The novelty lies in its two-stage action-selection process. After the value-update step, the agent first **updates its policy explicitly**. It identifies the current greedy action (the one with the maximum Q(a)) and "pulls" the entire probability distribution of its policy towards that action. The probability of the greedy action is increased, while the probabilities of all other actions are proportionally decreased. Only after this policy update does the agent select its next move by sampling from this newly adjusted policy.