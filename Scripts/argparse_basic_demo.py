#!/usr/bin/env python

import argparse


# For more info refer
# 1. https://www.pythonforbeginners.com/argparse/argparse-tutorial
# 2. https://docs.python.org/3/library/argparse.html

def parse_arguments():
    """
    This method will parse arguments and returns the arguments
    """
    global args
    parser = argparse.ArgumentParser(description='Argument parser for accepting two numbers to perform addtions')
    parser.add_argument("number", type=int, nargs='+', help="Enter atleast one number")
    parser.add_argument('--add', default=False, action="store_true")
    parser.add_argument('--mul', default=False, action="store_true")
    args = parser.parse_args()


def execute():
    """
    This method executes the logic of addition or multiplication
    """
    parse_arguments()
    numbers = args.number
    if args.add:
        result = 0
        for number in numbers:
            result = result + number
        print("Result of addition is {res}".format(res=result))
    elif args.mul:
        product = 1
        for number in numbers:
            product = product * number
        print("Result of addition is {res}".format(res=product))


if __name__ == '__main__':
    execute()
