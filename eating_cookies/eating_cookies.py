'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n, cache=[]):

    if len(cache) == 0:
        cache = [0] * (n + 1)

    # return eating_cookies_unoptimized(n)
    # return eating_cookies_optimized(n, cache)
    return eating_cookies_iterative(n)

def eating_cookies_iterative(n):

    # negative cookies left: not possible. Return 0 as a solution.
    if n < 0:
        return 0

    # exactly 0 cookies left: 1 solution found
    # exactly 1 cookie left: 1 way to eat
    elif n == 0 or n == 1:
        return 1

    # exactly 2 cookies left: 2 ways to eat
    elif n == 2:
        return 2

    # define recursive terms
    # start current term at 3 cookies to eat so all recursive terms are known
    ways_to_eat_n_minus_3_cookies = 1
    ways_to_eat_n_minus_2_cookies = 1
    ways_to_eat_n_minus_1_cookie = 2

    # define a variable to hold result (will compute value later)
    ways_to_eat_n_cookies = None

    # calculate current term based on previous two terms
    for i in range(3, n + 1):

        ways_to_eat_n_cookies = ways_to_eat_n_minus_3_cookies + ways_to_eat_n_minus_2_cookies + ways_to_eat_n_minus_1_cookie

        # update variables by shifting values over
        ways_to_eat_n_minus_1_cookie, ways_to_eat_n_minus_2_cookies, ways_to_eat_n_minus_3_cookies = ways_to_eat_n_cookies, ways_to_eat_n_minus_1_cookie, ways_to_eat_n_minus_2_cookies

    return ways_to_eat_n_cookies


def eating_cookies_optimized(n, cache):

    # negative cookies left: not possible. Return 0 as a solution.
    if n < 0:
        return 0

    # exactly 0 cookies left: 1 solution found
    # exactly 1 cookie left: 1 way to eat
    elif n == 0 or n == 1:
        return 1

    # look up precalculated values, or calculate from known values
    else:

        # the number ways to first eat 3 cookies at once + the number of ways to eat the remaining cookies
        ways_if_3_cookies_eaten_first = cache[n-3] if cache[n-3] != 0 else eating_cookies_optimized(n - 3, cache)

        # the number ways to first eat 2 cookies at once + the number of ways to eat the remaining cookies
        ways_if_2_cookies_eaten_first = cache[n-2] if cache[n-2] != 0 else eating_cookies_optimized(n - 2, cache)

        # the number ways to first eat a single cookie + the number of ways to eat the remaining cookies
        ways_if_1_cookie_eaten_first = cache[n-1] if cache[n-1] != 0 else eating_cookies_optimized(n - 1, cache)

        total_ways_for_n = ways_if_3_cookies_eaten_first + ways_if_2_cookies_eaten_first + ways_if_1_cookie_eaten_first

        # add to cache

        cache[n] = total_ways_for_n

        return total_ways_for_n


def eating_cookies_unoptimized(n):
    
    # negative cookies left: not possible. Return 0 as a solution.
    if n < 0:
        return 0

    # exactly 0 cookies left: 1 solution found
    # exactly 1 cookie left: 1 way to eat
    elif n == 0 or n == 1:
        return 1
    
    # the number of ways to eat n cookies (at most 3 at a time) is equal to...

    # the number of ways to first eat 3 cookies at once right now + and then eat the remaining cookies later
    ways_if_3_cookies_eaten_first = eating_cookies_unoptimized(n - 3)

    # the number of ways to first eat 2 cookies at once right now + and then eat the remaining cookies later
    ways_if_2_cookies_eaten_first = eating_cookies_unoptimized(n - 2)

    # the number of ways to first eat a single cookie right now + and then eat the remaining cookies later
    ways_if_1_cookie_eaten_first = eating_cookies_unoptimized(n - 1)

    return ways_if_3_cookies_eaten_first + ways_if_2_cookies_eaten_first + ways_if_1_cookie_eaten_first

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
