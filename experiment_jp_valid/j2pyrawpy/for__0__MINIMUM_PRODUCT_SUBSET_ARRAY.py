#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_PRODUCT_SUBSET_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def minProductSubset(cls, a, n):
        """ generated source for method minProductSubset """
        if n == 1:
            return a[0]
        negmax = Integer.MIN_VALUE
        posmin = Integer.MAX_VALUE
        count_neg = 0
        count_zero = 0
        product = 1
        if count_zero == n or (count_neg == 0 and count_zero > 0):
            return 0
        if count_neg == 0:
            return posmin
        if count_neg % 2 == 0 and count_neg != 0:
            product = product / negmax
        return product

