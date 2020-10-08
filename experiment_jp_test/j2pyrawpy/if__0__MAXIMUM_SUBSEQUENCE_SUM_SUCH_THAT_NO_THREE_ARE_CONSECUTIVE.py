#!/usr/bin/env python
""" generated source for module if__0__MAXIMUM_SUBSEQUENCE_SUM_SUCH_THAT_NO_THREE_ARE_CONSECUTIVE """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxSumWO3Consec(cls, arr, n):
        """ generated source for method maxSumWO3Consec """
        sum = [None]*n
        if n >= 2:
            sum[1] = arr[0] + arr[1]
        if n > 2:
            sum[2] = Math.max(sum[1], Math.max(arr[1] + arr[2], arr[0] + arr[2]))
        return sum[n - 1]

