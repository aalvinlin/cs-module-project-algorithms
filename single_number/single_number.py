'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    # return single_number_v1(arr)
    return single_number_v2(arr)

# Version 3: using 2 XORs on the same number will be cancelled out
def single_number_v3(arr):
    from functools import reduce
    return reduce(lambda x, y: x^y, arr)

# Version 2: use a set to store unique entries
def single_number_v2(arr):
    return 2 * sum(set(arr)) - sum(arr)

def single_number_v1(arr):
    # sort the array
    arr.sort()

    # look for a skip in pairs
    for i in range(0, len(arr), 2):
        if arr[i] is not arr[i + 1]:
            return arr[i]

import random
import time

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    arr = []

    for i in range(1000000):
        arr.append(i)
        arr.append(i)

    random.shuffle(arr)
    rand_index = random.randint(0, len(arr))
    num = arr.pop(rand_index)

    # time version 1
    start_time = time.time()
    result = single_number_v1(arr)
    end_time = time.time()

    elapsed_time_v1 = end_time - start_time

    # time version 2
    start_time = time.time()
    result = single_number_v2(arr)
    end_time = time.time()

    elapsed_time_v2 = end_time - start_time

    # time version 3
    start_time = time.time()
    result = single_number_v3(arr)
    end_time = time.time()

    elapsed_time_v3 = end_time - start_time

    print(f"The odd-number-out is {result}.")
    print(f"V1 computed in {elapsed_time_v1}.")
    print(f"V2 computed in {elapsed_time_v2}.")
    print(f"V3 computed in {elapsed_time_v3}.")


