'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    # return moving_zeroes_unoptimized(arr)
    return moving_zeroes_optimized(arr)

# optimized solution: single pass, O(1) storage
def moving_zeroes_optimized(arr):

    # use pointers to hold indices to next zero and next nonzero value
    index_of_next_zero = None

    for i in range(len(arr)):

        # set a pointer to the first zero in the array
        # the next nonzero value will be moved here
        if index_of_next_zero is None and arr[i] == 0:
            index_of_next_zero = i

        # if the first zero's location is known and the current value is nonzero, swap them
        # (use "is not None" because the index of the first zero could be at arr[0])
        if index_of_next_zero is not None and arr[i] != 0:
            arr[i], arr[index_of_next_zero] = arr[index_of_next_zero], arr[i]

            # the next value after the current zero is guaranteed to be a zero (if it were a number, it would have swapped to the front already)
            index_of_next_zero += 1

    return arr


def moving_zeroes_unoptimized(arr):
    
    # return just the nonzero values in the array
    nonzero_integers = [number for number in arr if number != 0]

    # pad with zeroes on the right
    return nonzero_integers + [0] * (len(arr) - len(nonzero_integers))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 0]
    arr = [1, 2, 3, 4, 5]
    arr = [1, 0, 0, 0, 2, 0, 3, 4, 5, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")