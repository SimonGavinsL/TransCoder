#!/usr/bin/env python
""" generated source for module for__0__FIND_THE_LARGEST_PAIR_SUM_IN_AN_UNSORTED_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def findLargestSumPair(cls):
        """ generated source for method findLargestSumPair """
        first = int()
        second = int()
        if arr[0] > arr[1]:
            first = arr[0]
            second = arr[1]
        else:
            first = arr[1]
            second = arr[0]
        return (first + second)

