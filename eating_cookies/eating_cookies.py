'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    
    return 2 ** (n-1) if n > 0 else 1

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
