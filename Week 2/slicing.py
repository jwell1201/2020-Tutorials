# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:23:50 2020

@author: alexa
"""

import numpy as np


xvec = np.array([1, 1])


def func(xvec):
    x, y = xvec  # Split inputs
    vector = np.zeros(2)
    vector[0] = x**4 + y**4 - 1
    vector[1] = x**2 - y**2 + 1
    return vector


def jacobianAnalytical(xvec):
    x, y = xvec
    matrix = np.zeros((2, 2))
    # First column
    matrix[0, 0] = 4*x**3  # df1/dx
    matrix[1, 0] = 2*x     # df2/dx
    # Second column
    matrix[0, 1] = 4*y**3  # df1/dy
    matrix[1, 1] = -2*y    # df2/dy
    return matrix


def jacobianNumerical(xvec):
    delta = 0.02
    matrix = np.zeros((2, 2))
    # First column
    matrix[:, 0] = (func(xvec + np.array([delta, 0])) - func(xvec)) / delta
    # Second column
    matrix[:, 1] = (func(xvec + np.array([0, delta])) - func(xvec)) / delta
    return matrix
