#!/bin/python3

def minimax(array):
    array.sort()
    total = 0
    for elements in array:
        total = total + elements

    minimum_sum = total - array[-1]
    maximum_sum = total - array[0]
    
    print (str(minimum_sum) + " " + str(maximum_sum))

def main():
    array = [int(element) for element in input().strip().split(' ')]
    minimax(array)

if __name__ == "__main__":
    main()
