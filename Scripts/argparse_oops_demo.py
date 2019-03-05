#!/usr/bin/env python

import argparse
import calculator

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
    calc = calculator.Calculator(numbers)
    if args.add:
        result = calc.add()
        print("Result of addition is {res}".format(res=result))
    elif args.mul:
        product = calc.mul()
        print("Result of addition is {res}".format(res=product))


if __name__ == '__main__':
    execute()
