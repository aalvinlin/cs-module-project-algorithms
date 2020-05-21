'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    return sliding_window_max_unoptimized(nums, k)
    # return sliding_window_max_optimized(nums, k)

def sliding_window_max_unoptimized(nums, k):

    # hold maxes for each window.
    total_maxes = len(nums) - k + 1
    maxes = [None] * total_maxes

    # calculate max for each window
    for i in range(total_maxes):

        lower_bound = i
        upper_bound = i + (k - 1)

        maxes[i] = max(nums[lower_bound:upper_bound + 1])

    return maxes

def sliding_window_max_optimized(nums, k):

    # hold maxes for each window
    maxes = []

    # store the current max value and its index    
    max_value = nums[0]
    max_index = 0

    # also store the second largest value and its index
    # if the max value is shifted off to the left, the new max will be either...
    # ...the second largest value in the existing window
    # ...the incoming value
    second_largest_value = None
    second_largest_index = None

    # the second largest value always needs to be known so it can potentially be upgraded to the max value
    # if the second largest value is shifted off to the left or if it is upgraded to max, the new second largest value will be either...
    # ...the third largest value in the existing window
    # ...the incoming value
    third_largest_value = None
    third_largest_index = None

    # all values would have to be known in this case...

    # find max for each sliding window
    for i in range(len(nums)):

        print(i)

        # if i < k, then the first sliding window hasn't started yet
        # take this time to find the max and second largest for the first sliding window (first k numbers)
        if i < k:

            # check if a larger value is coming in
            if nums[i] > max_value:

                # new value will be the max; old max will be the second largest
                second_largest_value = max_value
                second_largest_index = max_index

                max_value = nums[i]
                max_index = i

            # check if a larger second-largest is coming in. Update it if it exists
            elif second_largest_value and (nums[i] > second_largest_value):

                second_largest_value = nums[i]
                second_largest_index = i

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


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(sliding_window_max(arr, k))