#!/usr/bin/env python
""" generated source for module for__1__FIND_MAXIMUM_AVERAGE_SUBARRAY_OF_K_LENGTH """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMaxAverage(cls, arr, n, k):
        """ generated source for method findMaxAverage """
        if k > n:
            return -1
        csum = [None]*n
        csum[0] = arr[0]
        max_sum = csum[k - 1]
        max_end = k - 1
        return max_end - k + 1

