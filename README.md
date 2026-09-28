# CSPC: Computer Science for Physicists
## PW1 - Lab B: Data, Plotting, and Automation

### Data Analysis & Visualization
The observed data shows exponential decay behavior starting from an initial count of 5000. Comparing the side-by-side plots, the observed data points closely match the analytical decay law $N(t) = N_0 e^{-\lambda t}$ ($\lambda = 0.3$).

### Workflow Automation
The Snakemake pipeline automates figure generation by tracking dependencies between `decay_observed.csv` and `figure.png`, executing `plot.py` only when input files are modified.

## PW1 - Lab A: Radioactive Decay Simulation

### Overview
This repository contains the implementation of a radioactive decay simulation using Python and NumPy, featuring automated testing with PyTest and environment reproducibility with Conda.

### Performance Benchmarks (`speed.py`)
- **Pure Python Loop Execution Time**: `1.7994 s`
- **NumPy Vectorized Execution Time**: `0.0002 s`
- **Speed-up Factor**: NumPy implementation is approximately **10482.93x faster**.

### Testing
All automated unit tests pass successfully:
```bash
pytest -v