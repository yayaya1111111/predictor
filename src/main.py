import argparse


class predictor:

    def parser():
        parse = argparse.ArgumentParser(description="A program dedicated to predict future market prices")
        parse.add_argument("filename")
        arguments = parse.parse_args()
        print(arguments)

    def __init__(self):
        predictor.parser()
p = predictor()