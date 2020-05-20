'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):

    # hold maxes for each window
    maxes = []

    # store the current max value and its index    
    max_value = nums[0]
    max_index = 0

    # also store the second largest value and its index
    # if the max value is shifted off to the left, the second largest value will become the max
    second_largest = None
    second_largest_index = None

    # find max for each sliding window
    for i in range(len(nums)):

        # if i < k, then the first sliding window hasn't started yet
        # take this time to find the max and second largest for the first sliding window (first k numbers)
        if i < k:

            if nums[i] > max_value:
                max_value = nums[i]
                max_index = i

        # each time the window shifts over to the right, determine if the max needs to be updated
        # also determine if second_largest needs to be updated
        else:
            pass

    return maxes

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
