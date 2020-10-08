#!/usr/bin/env python
""" generated source for module for__0__SMALLEST_SUBSET_SUM_GREATER_ELEMENTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def minElements(cls, arr, n):
        """ generated source for method minElements """
        halfSum = 0
        halfSum = halfSum / 2
        Arrays.sort(arr)
        res = 0
        curr_sum = 0
        i = n - 1
        while i >= 0:
            curr_sum += arr[i]
            res += 1
            if curr_sum > halfSum:
                return res
            i -= 1
        return res

