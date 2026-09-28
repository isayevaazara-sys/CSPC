import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3

# TODO 1: Read decay_observed.csv into t and observed
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# TODO 2: Set N0 to first observed value and compute analytical decay
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: Create 1x2 subplot with shared axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

ax1.scatter(t, observed, color='blue', label='Observed')
ax1.set_title('Observed Data')
ax1.set_xlabel('Time')
ax1.set_ylabel('Count')
ax1.grid(True)

ax2.plot(t, analytical, color='red', label='Analytical')
ax2.set_title('Analytical Decay')
ax2.set_xlabel('Time')
ax2.grid(True)

plt.tight_layout()

# TODO 4: Save figure as figure.png
plt.savefig("figure.png")
print("figure.png successfully generated!")