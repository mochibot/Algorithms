#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# My initial naive solution
# def eating_cookies(n):
#    if n <= 0:
#        return 1
#    if n <= 2:
#        return n
#    else:
#        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)

# with cache implemented
def eating_cookies(n, cache=None):
    if n <= 0:
        return 1

    if n <= 2:
        return n
    
    if cache:
        if cache[n]:
            return cache[n]
        else:
            cache[n] = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache)
            return cache[n]
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')