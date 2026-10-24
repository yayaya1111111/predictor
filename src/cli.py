import argparse


def parser():
    parse = argparse.ArgumentParser(description="A program dedicated to predict future market prices")
    parse.add_argument("filename", help="A CSV-formatted file of previous price data")
    arguments = parse.parse_args()
    print(arguments)    
    return arguments