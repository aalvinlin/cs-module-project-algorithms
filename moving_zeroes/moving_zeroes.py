'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    # return just the nonzero values in the array
    nonzero_integers = [number for number in arr if number is not 0]

    # pad with zeroes on the right
    return nonzero_integers + [0] * (len(arr) - len(nonzero_integers))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")