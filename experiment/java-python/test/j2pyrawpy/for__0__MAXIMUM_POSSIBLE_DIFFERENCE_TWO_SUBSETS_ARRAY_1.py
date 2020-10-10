#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_POSSIBLE_DIFFERENCE_TWO_SUBSETS_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxDiff(cls, arr, n):
        """ generated source for method maxDiff """
        result = 0
        Arrays.sort(arr)
        if arr[n - 2] != arr[n - 1]:
            result += Math.abs(arr[n - 1])
        return result

