#!/bin/python3

def birthdayCakeCandles(candles):
    maximum_height = max(candles)
    print (candles.count(maximum_height))

def main():
    number_of_candles = int(input())
    candles = [int(candle) for candle in input().strip().split(' ')[:number_of_candles]]
    birthdayCakeCandles(candles)

if __name__ == "__main__":
    main()
