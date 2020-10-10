#!/usr/bin/env python
""" generated source for module if__0__FIND_MAXIMUM_PRODUCT_OF_A_TRIPLET_IN_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxProduct(cls, arr, n):
        """ generated source for method maxProduct """
        Arrays.sort(arr)
        return Math.max(arr[0] * arr[1] * arr[n - 1], arr[n - 1] * arr[n - 2] * arr[n - 3])

