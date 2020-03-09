#!/bin/python3

def appendAndDelete(initial_string, target_string, number_of_operations):
    
    if number_of_operations >= len(initial_string) + len(target_string) : return "Yes"

    i = 0
    minimum_cost = min(len(initial_string), len(target_string))
    while i < minimum_cost and initial_string[i] == target_string[i]: i += 1    
    cost = len(initial_string)-i + len(target_string)-i
        
    if number_of_operations < cost : return "No"
    if number_of_operations == cost : return "Yes"
    
    if (number_of_operations-cost)%2:
        return "No"     
    else:
        return "Yes"
    

def main():
    initial_string = input()
    target_string = input()
    number_of_operations = int(input())
    result = appendAndDelete(initial_string, target_string, number_of_operations)
    print (result)

if __name__ == "__main__":
    main()
