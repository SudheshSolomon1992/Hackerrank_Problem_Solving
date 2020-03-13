#!/bin/python3
from datetime import datetime
from dateutil import relativedelta

def calculate_fine (difference, year_r, year_d, month_d, month_r):
    fine = 0
    flag = str(difference)[14:].replace(')', '')

    if '+' in str(difference) or ('days' not in flag and 'months' not in flag and 'years' not in flag):
        return 0

    elif int(year_d) != int(year_r):
        return 10000
            
    elif 'days' in flag and 'months' not in flag and 'years' not in flag:
        difference = flag.split(',')[0].split('=')[1]
        fine = abs(int(difference)) * 15
        return fine
    else:
        if "months" in flag and 'days' in flag and 'years' not in flag:
            difference = abs(int(month_d - month_r))
            fine = abs(int(difference)) * 500 
            return fine
            
        else:
            pass

def main():
    returned = [element for element in input().strip().split(' ')]
    due = [element for element in input().strip().split(' ')]
    
    day_r = int(returned[0])
    month_r = int(returned[1])
    year_r = int(returned[2])
    r = datetime (year_r, month_r, day_r)
    
    day_d = int(due[0])
    month_d = int(due[1])
    year_d = int(due[2])
    d = datetime (year_d, month_d, day_d)

    difference = relativedelta.relativedelta(d, r)
    fine = calculate_fine (difference, year_d, year_r, month_d, month_r)
    
    print (fine)
    
if __name__ == "__main__":
    main()
