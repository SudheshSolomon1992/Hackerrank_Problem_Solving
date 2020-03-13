#!/bin/python3

def cutTheSticks(length_array):
    cut_length = min(length_array)
    __temp = []
    for stick in length_array:
        stick = stick - cut_length
        if stick != 0:
            __temp.append(stick)
           
    if len(__temp) != 0:
        print (len(__temp))
        cutTheSticks(__temp)

def main():
    number_of_sticks = int(input())
    length_of_sticks = [int(length) for length in input().strip().split(' ')[:number_of_sticks]]
    print (number_of_sticks)
    cutTheSticks(length_of_sticks)

if __name__ == "__main__":
    main()
