#!/bin/python3

def staircase(dimension):
    element = ''
    array = []
    count = dimension
    for __temp in range(dimension):
        padding = (count-1) * ' '
        element = element + '#'
        array.append(padding + element)
        count = count - 1

    for element in array:
        print (element)

def main():
    dimension = int(input())
    staircase(dimension)

if __name__ == "__main__":
    main()
