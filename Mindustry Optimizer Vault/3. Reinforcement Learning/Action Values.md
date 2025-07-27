[[1.RL]]


As an overview, we can understand simple reinforcement learning agents as having two primary aspects: a **learning mechanism(critic)** and an **action-selection mechanism(actor)**. The learning mechanism is responsible for tracking the value or desirability of actions, effectively creating the agent's internal representation of the world. The action-selection mechanism then transforms this internal representation into "movement," or a concrete decision on how to act.

Action Value methods:
Stationary 

1. Sample Average 1/k weighted difference
Non-Stationary
 - recency-weighted average 1/c weighted difference
	 - **Exercise 2.6 (General Step-Sizes):** We've done this one. The key idea is that the weight on a past reward is its own step-size, multiplied by a "forgetting factor" for every step that came after it.

Action Selection:
1. Soft max Selection: soft max which is a the way to make the probabilities between actions more accentuated and making it relative so its out of 1 and transformed from negative numbers. Which also chooses weighted by the outputted probabilities of the soft max.
2. Greedy
3. Epsilon Greedy
4. Optimistic Greedy

Policies are just emergent behaviors from the action selection mechanism

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

- **Exercise 2.8 (Optimistic Initial Values):** Why do the performance curves for this method have those early spikes and wiggles, even when averaged over 2000 runs? (Hint: Think about what the agent is forced to do at the very beginning).
	- Since the initial values are higher than the expected true value by the actor being greedy or some form of it it will naturally pick through the initial high values which will converge to the truth given the critic. Since the actor is greedy it will continuously select the greedy option which means it will rotate through the "best" action until the other actions converge to a value lower than it. At least this was my initial intuition.
- **Refinement for the "Spikes":** Why the spikes and oscillations? The "wiggles" are the systematic exploration you described. The "spikes" happen when, by pure random chance, an arm gives an unusually high reward on its first pull. This makes its updated value drop less than the others, so the agent might stick with it for a few pulls before its value finally drops enough to encourage exploring another arm. This temporary "stickiness" to a lucky arm, averaged over 2000 runs, creates the early spikes in performance.



2.8 Reinforcement comparison:
Reinforcement Comparison introduces a novel agent architecture. Its core component is a "rolling indicator," the **reference reward (r_bar)**, which serves as a baseline to judge whether a new reward is better or worse than the agent's recent average experience. This r_bar is typically a recency-weighted average of all rewards the agent has received.

The learning rule in RC is unique: it does not learn or store long-term action-values (Q(a)). Instead, an individual reward is used only momentarily to update a **preference** for the action taken. The preference update, p(a) ← p(a) + α(R - r_bar), is structurally similar to a traditional value update, but it operates on preferences relative to the global r_bar baseline. This creates a sort of hierarchy where actions are judged not on their absolute merit, but on their performance relative to the agent's overall average. These learned preferences are then fed into a softmax function to produce a policy from which the next action is selected.

- **Exercise 2.9 (RC & Softmax Temperature):** Why is the temperature parameter τ often left out of the softmax function when using RC with preferences p(a)? (Hint: How else can you control the greediness of the policy?)  Oh because due to the actions having a an inherit rating (preference) via the critic the preferences encode the actions hierarchy relative to fbar so by selecting whichever is not arg max you are being explorative.
- *My* *refinement*: **(Soft max chooses randomly from the set of actions weighted by probabilities so by influencing the learning step since that reflects how much of the difference between action reward and f bar is added or subtracted from preference.)**

**Critique:** You're on the right track by thinking about the preferences, but the reasoning is slightly off. Softmax always explores by definition (unless τ=0). The real question is why τ is a redundant parameter. 



**Refinement:** The **greediness** of the final policy depends on the magnitude of the differences between the preferences p(a).

- If preferences are [10, 8, 1], the policy will be very greedy.
- If preferences are [0.1, 0.08, 0.01], the policy will be very exploratory.
    
In RC, the magnitude of these preferences is controlled by the learning rate α. A large α leads to big preference updates and thus big differences. A small α leads to small updates and small differences. Since α already controls the spread of preferences, adding a τ to also control the spread is redundant. You can achieve the same effect by just tuning α.


- **Exercise 2.10 (RC & Step-Size Parameters):** Imagine you have two learning rates, α for preferences and β for the reference reward r_bar. What is the downside of forcing them to be the same (α = β)? (Hint: Do you always want to update your baseline standard at the same speed you react to a surprise?) That the basis of measurement would be very sporadic meaning that the next action to be choose has to explicitly be greater than the current action since the f bar will become that current reward. So action convergence is probably very hard especially in a non-stationary environment.

**Critique:** **Excellent intuition!** You've perfectly captured the problem.
**Refinement:** Let's put formal names on it. You need to control the speed of two different learning processes:

1. **Reacting to a surprise:** How much does one good/bad reward affect an action's preference? This is controlled by α. You might want this to be high to learn quickly.
    
2. **Updating your worldview:** How much does one reward affect your overall baseline of what's "normal"? This is controlled by β. You probably want this to be very low, so your r_bar is stable and not "sporadic," as you put it.  
    Forcing α = β means if you want to react quickly to surprises (high α), you are also forced to have a very unstable baseline (high β), which makes the whole system chaotic. You lose the flexibility to have a stable worldview while still being sensitive to new information.


2.9 Pursuit method:
In contrast, the Pursuit Method can be concisely described as a more dynamic greedy approach. It uses a conventional learning rule to update its estimates of long-term action-values, Q(a).

The novelty lies in its two-stage action-selection process. After the value-update step, the agent first **updates its policy explicitly**. It identifies the current greedy action (the one with the maximum Q(a)) and "pulls" the entire probability distribution of its policy towards that action. The probability of the greedy action is increased, while the probabilities of all other actions are proportionally decreased. Only after this policy update does the agent select its next move by sampling from this newly adjusted policy.

- **Exercise 2.12 (Pursuit & Exploration):** A simple ε-greedy agent never stops exploring. Does the pursuit algorithm have this same property? Why or why not? (Hint: Look at the policy update rule. What happens to the probabilities over time?) ~~Potentially not~~  They converge since the update rule simultaneously increases the arg max and decreases all the others. 



- **Exercise 2.13 (Pursuit with Preferences):** This is a pure design question. How would you redesign the pursuit algorithm if it couldn't directly touch the policy probabilities π(a)? Your agent's "brain" now stores Q(a) and p(a). How do you make the preferences p(a) "chase" the greedy action A*? Don't you just apply the same idea of increase and decrease but to the action values i suppose that the explicit value or decrease could just be a constant instead of trying a 1- for the addition. 

**Critique:** **You have designed a perfectly valid and excellent solution!** You're applying the core idea of pursuit to the preferences.

**Refinement (The formal design):**

1. Learn Q-values Q(a) as normal 
2. Identify the greedy action $A* = argmax Q(a)$.
3. Update the **preferences** $p(a)$ to "pursue" $A*$. Your idea of a constant is great. A simple rule could be:
    - $p(A*) ← p(A*) + β$ (where β is a small "pursuit rate")   
    - For all other actions $a ≠ A*$, you could do $p(a) ← p(a) - β/(n-1)$ $n$ (being total actions) to ensure the total "preference mass" stays constant, or just leave them. The key is to increase the preference for the greedy action.    
4. Select an action using softmax on the new preferences $p(a)$.
    
- **Exercise 2.15 (Pursuit & ε-greedy):** How would you combine the two ideas to get the best of both worlds: a policy that actively chases the greedy action but also never completely stops exploring? (Hint: Think about where in the action-selection pipeline you could inject a little bit of randomness). probably in the update rule you could on top of the decrease and increase also add a random noise or even make the step random noise.

**Critique:** That's a very creative idea! Adding noise to the update rule is a valid way to encourage exploration, related to techniques used in evolutionary algorithms. However, there's a more direct and standard way to combine the two ideas.

**Refinement:** Think about the **output** of the pursuit method. It's a policy π. The ε-greedy method is also a policy. We can layer them. The simplest combination is:

1. Perform the entire pursuit method update to get a policy π_pursuit.
2. Now, use this policy as the "greedy" part of ε-greedy.
    - With probability (1-ε), choose an action by sampling from π_pursuit.
    - With probability ε, choose a random action from all n options.  
        This guarantees you mostly follow the smart pursuit strategy but always retain a small ε chance of trying something completely new.

2.10 Associative Search
Basically if given an  environment such that there exist different situations then a mapping between actions and situations exist, this is also known as a policy. Given this the process begins of finding the best action given the situation and consistently mapping and tracking these over time. 

- **Exercise 2.16 (Associative Search):** This is the capstone conceptual question.
    
    - **Part A:** You face a bandit where the rewards are randomly (0.1, 0.2) or (0.9, 0.8), but you don't know which case it is. What is the best you can do on average? I figure since on average you dont know the case and considering that the result is the combination of several passes over several cases i would imagine a simple average would give me the answer so between   4- 5 thinking about just adding each value and dividing by 2 if that makes sense 
        
    - **Part B:** Now, before each play, you are told whether you are in "Case A" or "Case B". How does your strategy change? What is your new, higher average score? This demonstrates why having "state" information is so powerful. In this case my average would be 11/2 since knowing my case implies that i know the optimal choice so simply using a greedy associative model would result in 9 and 2 being choosen.