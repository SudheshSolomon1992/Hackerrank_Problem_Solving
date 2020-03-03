#!/bin/python3

def calculate_sum(array):
    sum = 0 
    
    for elements in array:
        sum = sum + elements
    
    return sum

def main():
    number_of_elements = int(input())
    elements = [int(numbers) for numbers in input().strip().split(' ')[:number_of_elements]]
    result = calculate_sum(elements)
    print (result)

if __name__ == "__main__":
    main()
