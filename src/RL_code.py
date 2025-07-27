import numpy as np
import matplotlib.pyplot as plt

class BanditTestbed:
    """
    A class to represent the 10-armed bandit testbed environment.
    From Sutton & Barto, Chapter 2, Figure 2.1.
    """
    def __init__(self, k=10, seed=None):
        """
        Initializes the testbed.
        Args:
            k (int): Number of arms (bandits).
            seed (int): Optional random seed for reproducibility.
        """
        if seed is not None:
            np.random.seed(seed)
            
        self.k = k
        # The true action values, q*(a), are selected from a normal distribution
        # with mean 0 and variance 1.
        self.q_true = np.random.randn(k)
        # The optimal action is the one with the highest true value.
        self.optimal_action = np.argmax(self.q_true)

    def step(self, action):
        """
        Simulates taking an action (pulling an arm).
        Args:
            action (int): The index of the arm to pull.
        Returns:
            float: The reward, selected from a normal distribution with mean
                   q*(action) and variance 1.
        """
        reward = np.random.randn() + self.q_true[action]
        return reward

def epsilon_greedy_policy(q_estimates, epsilon):
    """Selects an action using the epsilon-greedy policy."""
    if np.random.random() < epsilon:
        # Explore: choose a random action
        return np.random.randint(len(q_estimates))
    else:
        # Exploit: choose the action with the highest estimated value
        return np.argmax(q_estimates)

def softmax_policy(q_estimates, temperature):
    """Selects an action using the softmax (Gibbs) distribution."""
    # To prevent overflow with large Q-values, subtract the max
    q_estimates = q_estimates - np.max(q_estimates)
    
    probabilities = np.exp(q_estimates / temperature)
    probabilities /= np.sum(probabilities)
    
    # Choose an action based on the calculated probabilities
    return probabilities

def run_experiment(k, num_steps, num_runs, policy_func, policy_param, alpha):
    """
    Runs a full bandit experiment.
    
    Args:
        k (int): Number of arms.
        num_steps (int): Number of steps per run.
        num_runs (int): Number of independent runs to average over.
        policy_func (function): The policy to use (e.g., epsilon_greedy_policy).
        policy_param (float): The parameter for the policy (epsilon or temperature).
        alpha (float): The step-size for the Q-value updates.
        
    Returns:
        tuple: (average_rewards, optimal_action_percentages)
    """
    # Arrays to store the results, averaged over all runs
    avg_rewards = np.zeros(num_steps)
    optimal_action_counts = np.zeros(num_steps)

    for run in range(num_runs):
        if run % 200 == 0:
            print(f"Running {policy_func.__name__} (param={policy_param})... Run {run}/{num_runs}")
            
        testbed = BanditTestbed(k=k) # Create a new problem for each run
        q_estimates = np.zeros(k)   # Agent's value estimates (Q), reset for each run
        
        for step in range(num_steps):
            # 1. Select action using the policy
            action = policy_func(q_estimates, policy_param)
            
            # 2. Get reward from the environment
            reward = testbed.step(action)
            
            # 3. Update the agent's value estimate for the chosen action
            # Q_new = Q_old + alpha * [Reward - Q_old]
            q_estimates[action] += alpha * (reward - q_estimates[action])
            
            # Store results for this step
            avg_rewards[step] += reward
            if action == testbed.optimal_action:
                optimal_action_counts[step] += 1
                
    # Average the results over all runs
    avg_rewards /= num_runs
    optimal_action_percentages = (optimal_action_counts / num_runs) * 100
    
    return avg_rewards, optimal_action_percentages

def RC_re(k,steps,runs, alpha,beta,modified):
    avg_rewards = np.zeros(steps)
    optimal_action_counts = np.zeros(steps)
 
    for run in range(runs):
        if run % 200 == 0:
            print(f"Running RC agent (modified{modified})... Run {run}/{runs}")
        testbed = BanditTestbed(k=k) # Create a new problem for each run

        f_bar = 0.0
        p_estimates = np.zeros(k)
        for step in range(steps):
            # use soft max on prefernces with tau 1
            probabilities = softmax_policy(p_estimates, 1)
            action = np.random.choice(len(p_estimates), p=probabilities)
            
            # return reward from selected action from soft max
            reward = testbed.step(action)
            # pass value estimates, action, reward and beta
            f_bar = f_bar + beta*(reward - f_bar)

            if modified:
                update_rule = alpha*(reward - f_bar)*(1 - probabilities[action])
            else:
                update_rule =  alpha*(reward - f_bar)

            # calculate new preference
            p_estimates[action] = p_estimates[action] + update_rule

            avg_rewards[step] += reward
            if action == testbed.optimal_action:
                optimal_action_counts[step] += 1
                
    # Average the results over all runs
    avg_rewards /= runs
    optimal_action_percentages = (optimal_action_counts / runs) * 100
        
    return avg_rewards, optimal_action_percentages

def preference_pursuit(k,steps, runs, alpha, beta):
    avg_rewards = np.zeros(steps)
    optimal_action_counts = np.zeros(steps)
 
    for run in range(runs):
        if run % 200 == 0:
            print(f"Running Preference Pursuit Agent)... Run {run}/{runs}")
        testbed = BanditTestbed(k=k) # Create a new problem for each run

        p_estimates = np.zeros(k)
        q_estimates = np.zeros(k)

        for step in range(steps):
            # use soft max on prefernces with tau 1
            probabilities = softmax_policy(p_estimates, 1)
            action = np.random.choice(len(p_estimates), p=probabilities)
            # return reward from selected action from soft max
            reward = testbed.step(action)
            # update f_bar and action values
            q_estimates[action] = q_estimates[action] + alpha*(reward - q_estimates[action])

            greedy = np.argmax(q_estimates)

            # apply pursuit logic 
            p_estimates[greedy] += beta
            pursuit_update = np.arange(len(p_estimates)) != greedy
            p_estimates[pursuit_update] -= 1/beta
            
            avg_rewards[step] += reward
            if action == testbed.optimal_action:
                optimal_action_counts[step] += 1
                
    # Average the results over all runs
    avg_rewards /= runs
    optimal_action_percentages = (optimal_action_counts / runs) * 100
        
    return avg_rewards, optimal_action_percentages

class NonStationaryBanditTestbed(BanditTestbed):
    """
    A class to represent issue with Sample averages in nonstationary enviroments
    """

    def __init__(self, k=10, seed=None):
        super().__init__(k, seed)
        self.q_true = np.zeros(k)
        self.optimal_action = np.argmax(self.q_true)

    def step(self,action):
        reward = np.random.randn() + self.q_true[action]
        self.q_true += np.random.normal(loc=0, scale=0.01, size=self.k)
        self.optimal_action = np.argmax(self.q_true)

        return reward

def run_experiment(k, num_steps, num_runs, policy_func, policy_param, alpha,sample_average):
    """
    Runs a full bandit experiment.
    
    Args:
        k (int): Number of arms.
        num_steps (int): Number of steps per run.
        num_runs (int): Number of independent runs to average over.
        policy_func (function): The policy to use (e.g., epsilon_greedy_policy).
        policy_param (float): The parameter for the policy (epsilon or temperature).
        alpha (float): The step-size for the Q-value updates.
        
    Returns:
        tuple: (average_rewards, optimal_action_percentages)
    """
    # Arrays to store the results, averaged over all runs
    avg_rewards = np.zeros(num_steps)
    optimal_action_counts = np.zeros(num_steps)

    for run in range(num_runs):
        if run % 200 == 0:
            print(f"Running {policy_func.__name__} (param={policy_param})... Run {run}/{num_runs}")
            
        testbed = NonStationaryBanditTestbed(k=k) # Create a new problem for each run
        q_estimates = np.zeros(k)   # Agent's value estimates (Q), reset for each run
        q_action_counts = np.zeros(k)

        for step in range(num_steps):
            # 1. Select action using the policy
            action = policy_func(q_estimates, policy_param)

            q_action_counts[action] += 1
            
            # 2. Get reward from the environment
            reward = testbed.step(action)
            
            # 3. Update the agent's value estimate for the chosen action
            # Q_new = Q_old + alpha * [Reward - Q_old]
            if sample_average:
                q_estimates[action] += 1/q_action_counts[action] * (reward - q_estimates[action])
            else:
                q_estimates[action] += alpha * (reward - q_estimates[action])
            
            # Store results for this step
            avg_rewards[step] += reward
            if action == testbed.optimal_action:
                optimal_action_counts[step] += 1
                
    # Average the results over all runs
    avg_rewards /= num_runs
    optimal_action_percentages = (optimal_action_counts / num_runs) * 100
        
    
    return avg_rewards, optimal_action_percentages

if __name__ == '__main__':
    # --- Experiment Parameters ---
    K_ARMS = 2
    NUM_STEPS = 1000
    NUM_RUNS = 2000 # As used in the book for smooth curves
    ALPHA = 0.1     # Constant step-size

    # --- Run simulations ---
    # Epsilon-Greedy
    eps_01_rewards, eps_01_optimal = run_experiment(
        K_ARMS, NUM_STEPS, NUM_RUNS, epsilon_greedy_policy, 0.1, alpha=ALPHA,sample_average=True)
    
    #eps_001_rewards, eps_001_optimal = run_experiment(
    #    K_ARMS, NUM_STEPS, NUM_RUNS, epsilon_greedy_policy, 0.01, alpha=ALPHA)
        
    # Softmax
    #tau_01_rewards, tau_01_optimal = run_experiment(
       #K_ARMS, NUM_STEPS, NUM_RUNS, softmax_policy, 0.1, alpha=ALPHA)
        
    #tau_04_rewards, tau_04_optimal = run_experiment(
    #    K_ARMS, NUM_STEPS, NUM_RUNS, softmax_policy, 0.4, alpha=ALPHA)

    # Non-stationary tests

    # sample average
    #sa_rewards, sa_optimal = run_experiment(
        #K_ARMS, NUM_STEPS, NUM_RUNS, epsilon_greedy_policy, 0.01, 0,True)
    # constant
    # K_ARMS, NUM_STEPS, NUM_RUNS, epsilon_greedy_policy, 0.01, ALPHA,False)

    # classic RC 
    #cRC_rewards, cRC_optimal = RC_re(
        #K_ARMS, NUM_STEPS, NUM_RUNS, 0.1, 0.1,False)
    
    #modified Rc
   # mRC_rewards, mRC_optimal = RC_re(
       # K_ARMS, NUM_STEPS, NUM_RUNS, 0.1, 0.1,True)
    
    #preference-pursuit
    pp_rewards, pp_optimal = preference_pursuit( K_ARMS, NUM_STEPS, NUM_RUNS, 0.1, 0.1)

    # --- Plotting ---
    plt.figure(figsize=(12, 5))

    # Plot 1: Average Reward
    
    plt.subplot(1, 2, 1)
    plt.plot(eps_01_rewards, label='e greedy')
    plt.plot(pp_rewards, label='preference pursuit')
    #plt.plot(tau_01_rewards, label='Softmax (τ=0.1)')
    #plt.plot(tau_04_rewards, label='Softmax (τ=0.4)')
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')
    plt.title('Average Reward Comparison')
    plt.legend()
    plt.grid(True)
    

    # Plot 2: % Optimal Action
    plt.subplot(1, 2, 2)
    plt.plot(eps_01_optimal, label='e greedy')
    plt.plot(pp_optimal, label='preference pursuit')
    #plt.plot(tau_01_optimal, label='Softmax (τ=0.1)')
    #plt.plot(tau_04_optimal, label='Softmax (τ=0.4)')
    plt.xlabel('Steps')
    plt.ylabel('% Optimal Action')
    plt.title('% Optimal Action Comparison')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()