# -*- coding: utf-8 -*-
"""
Introductory tutorial on numpy basics.
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """Cubic function."""
    return x**3


# np.logspace(start, end, num_of_intervals) == [10**start -> 10**end]
x, h = 1, np.logspace(-1, -3, 50)

# HINT: Central difference method
# df/dx = (f(x+h) - f(x-h)) / (2*h) + O(h^2)

approx = (f(x+h) - f(x-h)) / (2*h)
exact  = 3 * x**2

error = np.abs(approx - exact)
print(f'{error}')

plt.loglog(h, error)
