#!/usr/bin/env python
""" generated source for module for__0__CHOCOLATE_DISTRIBUTION_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMinDiff(cls, arr, n, m):
        """ generated source for method findMinDiff """
        if m == 0 or n == 0:
            return 0
        Arrays.sort(arr)
        if n < m:
            return -1
        min_diff = Integer.MAX_VALUE
        first = 0
        last = 0
        return (arr[last] - arr[first])

