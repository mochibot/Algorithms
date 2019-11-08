#!/usr/bin/python

import sys

# recursive apprach, not efficient
def making_change_recursive(amount, denominations):
    
    if amount < 0:
        return 0
    
    if amount == 0:
        return 1
    
    ways = 0
    curr_index = 0
    for coin in denominations:
        if coin <= amount:
            curr_index += 1
            ways += making_change_recursive(amount - coin, denominations[:curr_index])

    return ways


# bottom-up approach
def making_change(amount, denominations):

    ways = [0] * (amount + 1)
    ways[0] = 1    #base case

    for coin in denominations:
        for num in range(coin, amount + 1):
            ways[num] += ways[num - coin]

    return ways[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")