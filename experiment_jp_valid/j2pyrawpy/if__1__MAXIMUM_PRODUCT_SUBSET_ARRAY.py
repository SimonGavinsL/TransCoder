#!/usr/bin/env python
""" generated source for module if__1__MAXIMUM_PRODUCT_SUBSET_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxProductSubset(cls, a, n):
        """ generated source for method maxProductSubset """
        max_neg = Integer.MIN_VALUE
        count_neg = 0
        count_zero = 0
        prod = 1
        if count_neg % 2 == 1:
            if count_neg == 1 and count_zero > 0 and count_zero + count_neg == n:
                return 0
            prod = prod / max_neg
        return prod

