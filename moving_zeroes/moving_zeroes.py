'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    return moving_zeroes_unoptimized(arr)
    return moving_zeroes_optimized(arr)

# optimized solution: single pass, O(1) storage
def moving_zeroes_optimized(arr):

    # use pointers to hold indices to next zero and next nonzero value
    index_of_next_zero = None
    index_of_next_nonzero_value = None

    for i in range(len(arr)):

        if arr[i] == 0:
            index_of_next_zero = i
        else:
            



def moving_zeroes_unoptimized(arr):
    
    # return just the nonzero values in the array
    nonzero_integers = [number for number in arr if number is not 0]

    # pad with zeroes on the right
    return nonzero_integers + [0] * (len(arr) - len(nonzero_integers))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")