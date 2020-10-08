#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_SUBARRAY_SUM_USING_PREFIX_SUM """
class X(object):
    """ generated source for class X """
    @classmethod
    def maximumSumSubarray(cls, arr, n):
        """ generated source for method maximumSumSubarray """
        min_prefix_sum = 0
        res = Integer.MIN_VALUE
        prefix_sum = [None]*n
        prefix_sum[0] = arr[0]
        i = 0
        while i < n:
            res = Math.max(res, prefix_sum[i] - min_prefix_sum)
            min_prefix_sum = Math.min(min_prefix_sum, prefix_sum[i])
            i += 1
        return res

