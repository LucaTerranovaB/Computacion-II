import argparse
import math
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f", action="store_true", help="Fork the process")
parser.add_argument("number", type=float, help="Number to calculate the square root")

args = parser.parse_args()

if args.f:
    pid = os.fork()
    if pid == 0:
        # Child process
        result = -math.sqrt(args.number)
        print(f"Negative square root of {args.number} is {result:.2f}")
    else:
        # Parent process
        result = math.sqrt(args.number)
        print(f"Positive square root of {args.number} is {result:.2f}")
else:
    result = math.sqrt(args.number)
    print(f"Square root of {args.number} is {result:.2f}")
