#!/usr/bin/env python
""" generated source for module if__0__MINIMIZE_THE_MAXIMUM_DIFFERENCE_BETWEEN_THE_HEIGHTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def getMinDiff(cls, arr, n, k):
        """ generated source for method getMinDiff """
        Arrays.sort(arr)
        ans = arr[n - 1] - arr[0]
        small = arr[0] + k
        big = arr[n - 1] - k
        temp = 0
        if small > big:
            temp = small
            small = big
            big = temp
        return Math.min(ans, big - small)

