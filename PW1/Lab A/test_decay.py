"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
import decay
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?




def test_starts_at_N0():
    """Check that simulation starts with initial population N0."""
    res = decay.simulate(10000, 0.4)
    assert res[0] == 10000

def test_negative_rate_raises_error():
    """Check that calling simulate with a negative rate raises ValueError."""
    with pytest.raises(ValueError):
        decay.simulate(1000, -0.4)

def test_simulation_average():
    """Check that simulation population decreases over time."""
    res = decay.simulate(10000, 0.4)
    assert res[-1] < res[0]
