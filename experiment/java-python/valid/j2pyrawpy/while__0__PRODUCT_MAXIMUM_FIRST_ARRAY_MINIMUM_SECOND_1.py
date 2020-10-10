#!/usr/bin/env python
""" generated source for module while__0__PRODUCT_MAXIMUM_FIRST_ARRAY_MINIMUM_SECOND_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def minMaxProduct(cls, arr1, arr2, n1, n2):
        """ generated source for method minMaxProduct """
        max = arr1[0]
        min = arr2[0]
        i = int()
        while i < n2:
            if arr2[i] < min:
                min = arr2[i]
            i += 1
        return max * min

