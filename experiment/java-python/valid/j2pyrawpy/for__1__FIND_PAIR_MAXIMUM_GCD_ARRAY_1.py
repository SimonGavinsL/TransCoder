#!/usr/bin/env python
""" generated source for module for__1__FIND_PAIR_MAXIMUM_GCD_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMaxGCD(cls, arr, n):
        """ generated source for method findMaxGCD """
        high = 0
        count = [None]*high + 1
        counter = 0
        i = high
        while i >= 1:
            while j <= high:
                if count[j] > 0:
                    counter += count[j]
                j += i
                if counter == 2:
                    return i
            counter = 0
            i -= 1
        return 1

