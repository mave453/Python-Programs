#!/usr/bin/env python3
import argparse
import sys

def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

def main():
    parser = argparse.ArgumentParser(description="Compute factorial of a non-negative integer.")
    parser.add_argument("n", type=int, help="non-negative integer")
    parser.add_argument("-r", "--recursive", action="store_true", help="use recursive implementation")
    args = parser.parse_args()

    try:
        if args.n < 0:
            raise ValueError("n must be non-negative")
        func = factorial_rec if args.recursive else factorial_iter
        print(func(args.n))
    except RecursionError:
        print("Recursion limit reached. Use iterative mode for large n.", file=sys.stderr)
        sys.exit(2)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()