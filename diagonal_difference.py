#!/bin/python3

def primary_diagonal(array):
    left_to_right = 0

    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                left_to_right = left_to_right + array[i][j]
        
    return left_to_right

def secondary_diagonal(array, dimension):
    right_to_left = 0

    for i in range(len(array)):
        for j in range(len(array)):
            if i + j == dimension - 1:
                right_to_left = right_to_left + array[i][j]

    return right_to_left

def main():
    array = []
    dimension = int(input())
    for rows in range(dimension):
        row = [int(element) for element in input().strip().split(' ')[:dimension]]
        array.append(row)

    sum_left_to_right = primary_diagonal(array)
    sum_right_to_left = secondary_diagonal(array, dimension)
    
    print (abs(sum_left_to_right - sum_right_to_left))

if __name__ == "__main__":
    main()
