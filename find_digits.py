#!/bin/python3

def findDigits(array):
    for integer in array:
        count = 0
        digits_array = []
        for digits in str(integer):
            digits_array.append(int(digits))
        for digit in digits_array:
            if digit != 0:
                if int(integer) % int(digit) == 0:
                    count = count + 1
            else:
                pass
        print (count)


def main():
    array = []
    number_of_test_cases = int(input())
    for __ in range(number_of_test_cases):
        test_cases = input() 
        array.append(test_cases)
    
    findDigits(array)

if __name__ == "__main__":
    main()
