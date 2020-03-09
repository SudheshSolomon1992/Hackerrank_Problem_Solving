#!/bin/python3
import math

def countSquares(lower_bound, upper_bound):
    sqrt_lb = math.ceil(math.sqrt(lower_bound))
    sqrt_ub = math.floor(math.sqrt(upper_bound))
    
    print(sqrt_ub - sqrt_lb + 1)

def main():
    number_of_test_cases = int(input())
    for __ in range(number_of_test_cases):
        bound_value = [int(element) for element in input().strip().split(' ')]
        lower_bound = bound_value[0]
        upper_bound = bound_value[1]
        countSquares(lower_bound, upper_bound)

if __name__ == "__main__":
    main()
