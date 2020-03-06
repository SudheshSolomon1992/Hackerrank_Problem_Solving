#!/bin/python3

from datetime import datetime

def counvert_to_24(time):
    time_12 = datetime.strptime(time, '%I:%M:%S%p')
    time_24 = str(time_12).split(' ')[1]
    print (time_24)

def main():
    time_12 = input()
    counvert_to_24(time_12)

if __name__ == "__main__":
    main()
