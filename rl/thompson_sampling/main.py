
from __future__ import print_function, division
from builtins import range

import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import beta # beta distribution
# used for drawing beta distribution for each bandit

# np.random.seed(2)
NUM_TRIALS = 2000
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class Bandit:
    def __init__(self, p):
        self.p = p

        # Beta(1, 1), gives uniform distribution, since we do not have any 
        # prior information about the winrates of the bandits 
        self.a = 1
        self.b = 1
        
        self.N = 0 # for information only, not needed by the bandit algo
    
    def pull(self):
        return np.random.random() < self.p # draw a sample from Beta(a, b)
    
    def sample(self):
        return np.random.beta(self.a, self.b)

    def update(self, x):
        # posterior becomes the prior on each iteration
        # in code, it means overwriting the values a and b
        self.a += x
        self.b += (1 - x)
        self.N += 1


def plot(bandits, trial):
    # x axis
    x = np.linspace(0, 1, 200) # 200 evenly spaced samples in the range [0, 1]
    for b in bandits:
        y = beta.pdf(x, b.a, b.b)
        plt.plot(x, y, label=f"real p: {b.p:.4f}, win rate = {b.a - 1}/{b.N}")
    plt.title(f"Bandit distributions after {trial} trials")
    plt.legend()
    plt.show()


def experiment():
    bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]

    sample_points = [5, 10, 20, 50, 100, 200, 500, 1000, 1500, 1999]
    rewards = np.zeros(NUM_TRIALS)
    
    bandits_selection_count = [0, 0, 0]
    
    for i in range(NUM_TRIALS):
        # Thompson sampling
        j = np.argmax([b.sample() for b in bandits])

        # plot the posteriors
        if i in sample_points:
            plot(bandits, i)
        
        # pull the arm for the bandit with the largest sample
        x = bandits[j].pull()

        # update rewards
        rewards[i] = x

        # update the distribution for the bandit whose arm we just pulled
        bandits[j].update(x)
        bandits_selection_count[j] += 1
    
    # print total reward
    print("total reward earned:", rewards.sum())
    print("overall win rate:", np.sum(rewards) / NUM_TRIALS)
    print("num times selected each bandit:", bandits_selection_count)
    
if __name__ == '__main__':
    experiment()