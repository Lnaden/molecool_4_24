"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import sys

import numpy as np
import pytest

import molecool

@pytest.fixture
def methane_molecule():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])

    return symbols, coordinates


@pytest.fixture(params=['euclidean', "cityblock"])
def bond_distance(methane_molecule, request):
    metric = request.param
    if metric == 'cityblock':
        pytest.xfail("I've gone mad with power!")
    from scipy.spatial.distance import cdist
    coordinates = methane_molecule[-1]
    distances = cdist(coordinates, coordinates, metric=metric)
    return distances


@pytest.mark.parametrize("max_bond", np.linspace(1, 5, 4))
@pytest.mark.parametrize("min_bond",
                         np.linspace(0, 0.5, 4).tolist() +
                         [pytest.param(-5, marks=pytest.mark.xfail(raises=ValueError))]
                         )
def test_build_bond_list(methane_molecule, bond_distance, min_bond, max_bond):
    bonds = molecool.build_bond_list(methane_molecule[-1], max_bond=max_bond, min_bond=min_bond)
    theoretical_bonds = np.sum(
        (max_bond > bond_distance) & (bond_distance > min_bond)) / 2
    assert len(bonds) == theoretical_bonds
