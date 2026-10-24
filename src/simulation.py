import math
import random


def math_engine(s0,mu,sigma,T,n_paths,seed):
    if s0 <= 0 or sigma < 0 or T < 0 or n_paths <= 0:
        raise ValueError("s0, sigma, T, and n_paths must be non-negative")
    elif n_paths%1!=0:
        raise ValueError("n_paths must be integer")

    rng = random.Random(seed)
    drift = (mu - 0.5 * sigma ** 2) * T
    diffusion = sigma * math.sqrt(T)
    return [s0 * math.exp(drift + diffusion * rng.gauss(0, 1))
            for _ in range(n_paths)]

