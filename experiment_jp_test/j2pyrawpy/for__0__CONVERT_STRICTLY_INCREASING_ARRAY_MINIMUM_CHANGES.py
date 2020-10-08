#!/usr/bin/env python
""" generated source for module for__0__CONVERT_STRICTLY_INCREASING_ARRAY_MINIMUM_CHANGES """
class X(object):
    """ generated source for class X """
    @classmethod
    def minRemove(cls, arr, n):
        """ generated source for method minRemove """
        LIS = [None]*n
        len = 0
        i = 1
        while i < n:
            while j < i:
                if arr[i] > arr[j] and (i - j) <= (arr[i] - arr[j]):
                    LIS[i] = Math.max(LIS[i], LIS[j] + 1)
                j += 1
            len = Math.max(len, LIS[i])
            i += 1
        return n - len

