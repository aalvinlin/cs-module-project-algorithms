#!/usr/bin/python

import sys

def making_change(amount, denominations):
  
  # return making_change_unoptimized(amount, denominations)
  return making_change_optimized(amount, denominations)

def making_change_unoptimized(amount, denominations):

  # there is one way to make change for 0 cents
  # if this state is reached from a recursion call, then that means a solution was reached
  if amount == 0:
    return 1

  # if there is a negative number, then too much was subtracted from the previous step. Return 0
  elif amount < 0:
    return 0

  # no coins left but there is a positive amount of cents needed: return 0 ways
  elif len(denominations) == 0:
    return 0

  # total ways to make change:
  #   ways to make change with the largest coin used PLUS
  #   ways to make change without the largest coin used
  else:

    largest_coin_value = denominations[-1]

    return making_change_unoptimized(amount - largest_coin_value, denominations) + making_change_unoptimized(amount, denominations[:len(denominations) - 1]) 


# optimized version uses memoization to keep track of known values
def making_change_optimized(amount, denominations):

  print("finding ways to make change for", amount, "cents" )

  known_total_ways_to_make_change = {}

  answer = making_change_helper(amount, denominations, known_total_ways_to_make_change)

  print("calculated:", known_total_ways_to_make_change)

  return answer

def making_change_helper(amount, denominations, known_total_ways_to_make_change):

  # check to see if amount is stored yet. If so, return that value
  if amount in known_total_ways_to_make_change:

    print("memoization used!", amount, known_total_ways_to_make_change[amount])
    return known_total_ways_to_make_change[amount]

  # there is one way to make change for 0 cents
  # if this state is reached from a recursion call, then that means a solution was reached
  elif amount == 0:
    print("found a new way")
    return 1

  # if there is a negative number, then too much was subtracted from the previous step. Return 0
  elif amount < 0:
    return 0

  # no coins left but there is a positive amount of cents needed: return 0 ways
  elif len(denominations) == 0:
    return 0

  # total ways to make change:
  #   ways to make change with the largest coin used PLUS
  #   ways to make change without the largest coin used
  else:

    largest_coin_value = denominations[-1]

    ways_for_current_amount = making_change_helper(amount - largest_coin_value, denominations, known_total_ways_to_make_change) + making_change_helper(amount, denominations[:len(denominations) - 1], known_total_ways_to_make_change)

    # add newly computed number to store of known ways
    known_total_ways_to_make_change[amount] = ways_for_current_amount

    return ways_for_current_amount
  
if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")