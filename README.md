# CSPC: Computer Science for Physicists

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