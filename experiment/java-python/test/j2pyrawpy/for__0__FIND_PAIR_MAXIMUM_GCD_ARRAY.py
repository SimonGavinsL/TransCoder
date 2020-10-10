#!/usr/bin/env python
""" generated source for module for__0__FIND_PAIR_MAXIMUM_GCD_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMaxGCD(cls, arr, n):
        """ generated source for method findMaxGCD """
        high = 0
        divisors = [None]*high + 1
        i = 0
        while i < n:
            while j <= Math.sqrt(arr[i]):
                if arr[i] % j == 0:
                    divisors[j] += 1
                    if j != arr[i] / j:
                        divisors[arr[i] / j] += 1
                j += 1
            i += 1
        i = high
        while i >= 1:
            i -= 1
        return 1

