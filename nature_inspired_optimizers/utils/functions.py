import numpy as np

def uniform_random_vector(mean: float, scale: float, dimensions: int) -> np.ndarray:
    return np.random.uniform(mean - scale, mean + scale, dimensions)

def normal_random_vector(mean: float, scale: float, dimensions: int) -> np.ndarray:
    return np.random.normal(mean, scale, dimensions)