#!/bin/python3

def calculate_scores(alice_array, bob_array):
    alice = 0
    bob = 0
    if len(alice_array) == len(bob_array):
        for i in range(len(alice_array)):
            if alice_array[i] > bob_array[i]:
                alice = alice + 1
            elif alice_array[i] < bob_array[i]:
                bob = bob + 1
            else:
                alice = alice
                bob = bob
        print (str(alice) + " " + str(bob))
    else:
        print ("The lengths of both the arrays are different")

def main():
    alice_array = [int(alice_element) for alice_element in input().strip().split(' ')]
    bob_array = [int(bob_element) for bob_element in input().strip().split(' ')]
    calculate_scores(alice_array, bob_array)

if __name__ == "__main__":
    main()
