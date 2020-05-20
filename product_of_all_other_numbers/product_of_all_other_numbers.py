'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    return product_of_all_other_numbers_unoptimized(arr)
    # return product_of_all_other_numbers_optimized(arr)

def product_of_all_other_numbers_unoptimized(arr):

    # get product of all numbers in the array
    total_product = 1

    # determine if zeroes are present in this array
    zeroes_present = False

    # ignore zeroes when calculating product
    for n in arr:
        if n != 0:
            total_product *= n
        else:
            zeroes_present = True
    
    # calculate individual quotients in the answer
    # use total_product if the current number is zero
    if zeroes_present:
        return [total_product if n == 0 else 0 for n in arr]

    else:
        return [total_product // n for n in arr]

def product_of_all_other_numbers_optimized(arr):
    
    # O(n) time
    # no division used

    # O(n) space for now - need to reduce to O(1) space
    products = [1] * len(arr)
    
    # first pass: collect factors going from left to right
    running_factor = 1

    # multiply each number in the array by the factors so far
    for i in range (0, len(arr)):
        
        products[i] *= running_factor

        # collect factor at current index
        running_factor *= arr[i]

    # second pass: collect missing factors going from right to left
    running_factor = 1

    # multiply each number in the array by the factors so far
    for i in range (len(arr) - 1, -1, -1):
        
        products[i] *= running_factor

        # collect factor at current index
        running_factor *= arr[i]

    return products

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
