import numpy as np


def calculate_sample_mean(sample):
    return np.mean(sample)


def calculate_median(sample):
    return np.median(sample)


def calculate_half_sum_extreme(sample):
    return (min(sample) + max(sample)) / 2


def calculate_quantile(sample, index):
    return np.quantile(sample, index)


def calculate_half_sum_quantile(sample):
    return (calculate_quantile(sample, 0.25) + calculate_quantile(sample, 0.75)) / 2


def calculate_truncated_mean(sample):
    res = 0
    n = len(sample)
    r = int(0.25 * n)
    i = r + 1
    while i <= n - r:
        res += sample[i]
        i = i + 1
    return res / (n - 2 * r)


characteristic = {
    'sample_mean': calculate_sample_mean,
    'median': calculate_median,
    'half_sum_extreme': calculate_half_sum_extreme,
    'half_sum_quantile': calculate_half_sum_quantile,
    'truncated_mean': calculate_truncated_mean,
}


def get_characterisrics_template():
    characteristic_list = {
        'sample_mean': [],
        'median': [],
        'half_sum_extreme': [],
        'half_sum_quantile': [],
        'truncated_mean': [], }
    return characteristic_list
