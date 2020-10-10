#!/usr/bin/env python
""" generated source for module for__2__MAXIMUM_SUM_SUBARRAY_REMOVING_ONE_ELEMENT """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxSumSubarrayRemovingOneEle(cls, arr, n):
        """ generated source for method maxSumSubarrayRemovingOneEle """
        fw = [None]*n
        bw = [None]*n
        cur_max = arr[0]
        max_so_far = arr[0]
        fw[0] = arr[0]
        cur_max = max_so_far = bw[n - 1] = arr[n - 1]
        fans = max_so_far
        return fans

