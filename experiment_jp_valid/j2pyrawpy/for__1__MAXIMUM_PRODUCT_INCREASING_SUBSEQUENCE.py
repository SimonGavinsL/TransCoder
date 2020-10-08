#!/usr/bin/env python
""" generated source for module for__1__MAXIMUM_PRODUCT_INCREASING_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def lis(cls, arr, n):
        """ generated source for method lis """
        mpis = [None]*n
        max = Integer.MIN_VALUE
        k = 0
        while k < mpis.length:
            if mpis[k] > max:
                max = mpis[k]
            k += 1
        return max

