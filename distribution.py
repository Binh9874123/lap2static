from numpy import random
import numpy as np

loc, scale = 0.0, 1.0


def norm_distr(size):
    return random.normal(loc, scale, size)


def cauchy_distr(size):
    return random.standard_cauchy(size)


def laplace_distr(size):
    return random.laplace(loc, 1 / np.sqrt(2), size)


def poisson_distr(size):
    return random.poisson(10, size)


def uniform_distr(size):
    return random.uniform(-np.sqrt(3), np.sqrt(3), size)


distribution_fun = {'norm': norm_distr,
                    'cauchy': cauchy_distr,
                    'laplace': laplace_distr,
                    'poisson': poisson_distr,
                    'uniform': uniform_distr, }
