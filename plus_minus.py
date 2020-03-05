#!/bin/python3

def calculate_counts(number_of_elements,array):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for element in array:
        if "-" not in element and int(element) != 0:
            positive_count = positive_count + 1
        elif "-" in element and int(element) != 0:
            negative_count = negative_count + 1
        if len(element) == 1 and "0" in element:
            zero_count = zero_count + 1
        else:
            pass

    print ("{:.6f}".format(positive_count/number_of_elements))
    print ("{:.6f}".format(negative_count/number_of_elements))
    print ("{:.6f}".format(zero_count/number_of_elements))

def main():
    number_of_elements = int(input())
    array = [elements for elements in input().strip().split(' ')[:number_of_elements]]
    calculate_counts(number_of_elements, array)

if __name__ == "__main__":
    main()
