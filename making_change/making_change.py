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

  known_total_ways_to_make_change = {}

  return making_change_helper(amount, denominations, known_total_ways_to_make_change)

def making_change_helper(amount, denominations, known_total_ways_to_make_change):

  types_of_coins_available = len(denominations)

  # check to see if amount is stored yet. If so, return that value
  # there will be different answers based on the types of coins available
  #   ex: making change for 15 cents using [1, 5, 10]: 6 ways
  #   ex: making change for 15 cents using [1]: 1 way
  # dictionary lookup uses a tuple with both the amount and the types of coins available
  if (amount, types_of_coins_available) in known_total_ways_to_make_change:

    return known_total_ways_to_make_change[(amount, types_of_coins_available)]

  # there is one way to make change for 0 cents
  # if this state is reached from a recursion call, then that means a solution was reached
  elif amount == 0:
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

    ways_with_largest_coin_used = making_change_helper(amount - largest_coin_value, denominations, known_total_ways_to_make_change)
    ways_without_largest_coin_used = making_change_helper(amount, denominations[:len(denominations) - 1], known_total_ways_to_make_change)

    ways_for_current_amount = ways_with_largest_coin_used + ways_without_largest_coin_used

    # add newly computed number to store of known ways
    known_total_ways_to_make_change[(amount, types_of_coins_available)] = ways_for_current_amount

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