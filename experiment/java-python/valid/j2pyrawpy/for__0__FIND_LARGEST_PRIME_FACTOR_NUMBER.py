#!/usr/bin/env python
""" generated source for module for__0__FIND_LARGEST_PRIME_FACTOR_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxPrimeFactors(cls, n):
        """ generated source for method maxPrimeFactors """
        maxPrime = -1
        while n % 2 == 0:
            maxPrime = 2
            n >>= 1
        if n > 2:
            maxPrime = n
        return maxPrime

