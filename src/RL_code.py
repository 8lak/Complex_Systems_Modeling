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
    return np.random.choice(len(q_estimates), p=probabilities)

def run_experiment(k, num_steps, num_runs, policy_func, policy_param, alpha=0.1):
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


class NonStationaryBanditTestbed(BanditTestbed):
    """
    A class to represent issue with Sample averages in nonstationary enviroments
    """

    def __init__(self, k=10, seed=None):
        super().__init__(k, seed)
        self.q_true = np.zeros(k)

    def step(self,action):
        reward = super().step(action)
        self.q_true += np.random.normal(loc=0, scale=0.01, size=self.k)

        return reward

def run_experiment(k, num_steps, num_runs, policy_func, policy_param, alpha=0.1,sample_average=TRUE):
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

    if sample_average:
        
    
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
        K_ARMS, NUM_STEPS, NUM_RUNS, epsilon_greedy_policy, 0.1, alpha=ALPHA)
    
    eps_001_rewards, eps_001_optimal = run_experiment(
        K_ARMS, NUM_STEPS, NUM_RUNS, epsilon_greedy_policy, 0.01, alpha=ALPHA)
        
    # Softmax
    tau_01_rewards, tau_01_optimal = run_experiment(
        K_ARMS, NUM_STEPS, NUM_RUNS, softmax_policy, 0.1, alpha=ALPHA)
        
    tau_04_rewards, tau_04_optimal = run_experiment(
        K_ARMS, NUM_STEPS, NUM_RUNS, softmax_policy, 0.4, alpha=ALPHA)

    # --- Plotting ---
    plt.figure(figsize=(12, 5))

    # Plot 1: Average Reward
    
    plt.subplot(1, 2, 1)
    plt.plot(eps_01_rewards, label='ε-greedy (ε=0.1)')
    plt.plot(eps_001_rewards, label='ε-greedy (ε=0.01)')
    plt.plot(tau_01_rewards, label='Softmax (τ=0.1)')
    plt.plot(tau_04_rewards, label='Softmax (τ=0.4)')
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')
    plt.title('Average Reward Comparison')
    plt.legend()
    plt.grid(True)
    

    # Plot 2: % Optimal Action
    plt.subplot(1, 2, 2)
    plt.plot(eps_01_optimal, label='ε-greedy (ε=0.1)')
    plt.plot(eps_001_optimal, label='ε-greedy (ε=0.01)')
    plt.plot(tau_01_optimal, label='Softmax (τ=0.1)')
    plt.plot(tau_04_optimal, label='Softmax (τ=0.4)')
    plt.xlabel('Steps')
    plt.ylabel('% Optimal Action')
    plt.title('% Optimal Action Comparison')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()