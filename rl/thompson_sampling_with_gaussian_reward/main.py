
from __future__ import print_function, division
from builtins import range

import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm

# from scipy.stats import beta # beta distribution
# used for drawing beta distribution for each bandit

np.random.seed(1)
NUM_TRIALS = 2000
BANDIT_MEANS = [1, 2, 3]

class Bandit:
    def __init__(self, true_mean):
        # we are working with bandits with unknown mean and known precision
        # hence, 1 input argumen, the true mean
        # we assume precision of reward is 1 => variance is 1
        self.true_mean = true_mean
        #parameters for mu - prior is N(0, 1)
        # parameters to keep track of the posterior, which is technically now prior
        self.predicted_mean = 0 # mean of the mean of x
        self.lambda_ = 1 # prior is a standard normal(0, 1) <= normal(predicted_mean, 1/lambda)
        self.sum_x = 0 # for convenience, sum of all samples that we collect
        self.tau = 1 # preciion=1/variance?
        self.N = 0 # number of times we played this bandit
        
        
    def pull(self):
        # draws a sample from a normal distribution
        return np.random.randn() / np.sqrt(self.tau) + self.true_mean
    
    def sample(self):
        # draw a sample from posterior, also normal/gaussian
        return np.random.randn() / np.sqrt(self.lambda_) + self.predicted_mean

    def update(self, x):
        # cannot use recurrence, hence lengthy update
        self.lambda_ += self.tau # lambda = tau*N + lambda0
        self.sum_x += x
        self.predicted_mean = self.tau*self.sum_x / self.lambda_ # we do not have any prior for the mean,
            # we assume that the prior of the mean is zero
        self.N += 1


def plot(bandits, trial):
    # x axis
    x = np.linspace(-3, 6, 200) # 200 evenly spaced samples in the range [0, 1]
    for b in bandits:
        y = norm.pdf(x, b.predicted_mean, np.sqrt(1./b.lambda_))
        plt.plot(x, y, label=f"real mean: {b.true_mean:.4f}, num plays = {b.N}")
    plt.title(f"Bandit distributions after {trial} trials")
    plt.legend()
    plt.show()


def experiment():
    bandits = [Bandit(p) for p in BANDIT_MEANS]

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
    
    cumulative_average = np.cumsum(rewards) / (np.arange(NUM_TRIALS) + 1)
    # plot moving average ctr
    plt.plot(cumulative_average)
    for m in BANDIT_MEANS:
        plt.plot(np.ones(NUM_TRIALS)*m)
    plt.show()
    
    # print total reward
    print("total reward earned:", rewards.sum())
    print("overall win rate:", np.sum(rewards) / NUM_TRIALS)
    print("num times selected each bandit:", bandits_selection_count)
    
if __name__ == '__main__':
    experiment()