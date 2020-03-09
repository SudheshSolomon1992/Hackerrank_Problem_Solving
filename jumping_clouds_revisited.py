#!/bin/python3

def calculate_energy(array,number_of_elements,length_of_the_jump):
    energy = 100
    i = length_of_the_jump % number_of_elements #initial jump from 0
    energy -= array[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + length_of_the_jump) % number_of_elements
        energy -= array[i] * 2 + 1
        
    print (energy)

def main():
    data = input()
    number_of_elements = int(data.split(' ')[0])
    length_of_the_jump = int(data.split(' ')[1])
    array = [int(element) for element in input().strip().split(' ')[:number_of_elements]]
    calculate_energy (array, number_of_elements , length_of_the_jump)

if __name__ == "__main__":
    main()
