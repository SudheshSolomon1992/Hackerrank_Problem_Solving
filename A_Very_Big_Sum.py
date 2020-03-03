#!/bin/python3

def calculate_sum(array):
    element_sum = 0
    
    for elements in array:
        element_sum = element_sum + elements

    return element_sum

def main():
    number_of_elements = int(input())
    array = [int(elements) for elements in input().strip().split(' ')[:number_of_elements]]
    result = calculate_sum(array)
    print (result)

if __name__ == "__main__":
    main()
