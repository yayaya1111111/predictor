import argparse
import math
import random


class predictor:

    @staticmethod
    def parser():
        parse = argparse.ArgumentParser(description="A program dedicated to predict future market prices")
        parse.add_argument("filename", help="A CSV-formatted file of previous price data")
        arguments = parse.parse_args()
        print(arguments)    
        return arguments

    
    @staticmethod
    def math_engine(s0,mu,sigma,T,n_paths,seed):

        if s0 < 0 or sigma < 0 or T < 0 or n_paths < 0:
            raise ValueError("s0, sigma, T, and n_paths must be non-negative")

        rng = random.Random(seed)
        drift = (mu - 0.5 * sigma ** 2) * T
        diffusion = sigma * math.sqrt(T)
        return [s0 * math.exp(drift + diffusion * rng.gauss(0, 1))
                for _ in range(n_paths)]
    

    def __init__(self):
        predictor.parser()

p = predictor()
print(predictor.math_engine(100, 0, 0, 1, 10, 42))