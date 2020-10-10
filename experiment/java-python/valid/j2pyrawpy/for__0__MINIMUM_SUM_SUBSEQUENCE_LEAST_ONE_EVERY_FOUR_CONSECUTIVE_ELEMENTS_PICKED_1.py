#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def minSum(cls, ar, n):
        """ generated source for method minSum """
        if n <= 4:
            return Arrays.stream(ar).min().getAsInt()
        sum = [None]*n
        sum[0] = ar[0]
        sum[1] = ar[1]
        sum[2] = ar[2]
        sum[3] = ar[3]
        return Arrays.stream(Arrays.copyOfRange(sum, n - 4, n)).min().getAsInt()

