"""Provide the primary functions."""

import numpy as np

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote

def calculate_distance(rA, rB):
    # This function calculates the distance between two points given as numpy arrays.
    d = (rA - rB)
    dist = np.linalg.norm(d)
    return dist

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    if min_bond < 0:
        raise ValueError("Invalid minimum bond distance entered! Minimum bond distance must be greater than zero!")

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
