#!/bin/python3

def factorial(number):
    
    if (number == 1):
        return 1

    prod = number * factorial (number-1)
    return prod

def main():
    number = int(input())
    result = factorial(number)
    print (result)

if __name__ == "__main__":
    main()
