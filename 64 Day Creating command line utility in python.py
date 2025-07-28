# Day 64 -> Creating command line utility in python


import argparse
import sys 

def calc (args):
    if args.o=='add':
        return args.x+args.y
    elif args.o=='sub':
        return args.x-args.y
    elif args.o=='mul':
        return args.x*args.y
    elif args.o=='divide':
        return args.x/args.y
    else:
        return "Somethig went wrong"

if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument('--x', type=float,
                         default =1.0, help=" for 1 number This is the utiliy for manipulating numbers, please inform this roll number 24CS032")

    parser.add_argument('--y', type=float,
                         default =5.0, help=" for 2 number This is the utiliy for manipulating numbers, please inform this roll number 24CS032")

    parser.add_argument('--o', type=str,
                         default ="add", help=" This is the utiliy for calculations, please inform this roll number 24CS032")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))