#!/usr/bin/env python
""" generated source for module if__1__CEILING_IN_A_SORTED_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def ceilSearch(cls, arr, low, high, x):
        """ generated source for method ceilSearch """
        mid = int()
        mid = (low + high) / 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            if mid + 1 <= high and x <= arr[mid + 1]:
                return mid + 1
            else:
                return cls.ceilSearch(arr, mid + 1, high, x)
        else:
            if mid - 1 >= low and x > arr[mid - 1]:
                return mid
            else:
                return cls.ceilSearch(arr, low, mid - 1, x)

