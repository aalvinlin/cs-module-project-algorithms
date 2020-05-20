#!/usr/bin/python

import sys
from itertools import product

def rock_paper_scissors(n):
  # return rock_paper_scissors_unoptimized(n):
  return rock_paper_scissors_optimized(n)

def rock_paper_scissors_optimized(n):
  
  options = ["rock", "paper", "scissors"]

  return [list(sequence_of_moves) for sequence_of_moves in product(options, repeat=n)]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


print(rock_paper_scissors(4))