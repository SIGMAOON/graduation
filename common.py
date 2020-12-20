import numpy as np

def min_max_normalize(dataset):
    max_values = np.max(dataset, axis=0)
    normalized_dataset = dataset / max_values

    return normalized_dataset

def accuracy(predict, real):
    errors = np.abs(predict - real) / real
    mean_error = np.mean(errors)

    return 1 - mean_error