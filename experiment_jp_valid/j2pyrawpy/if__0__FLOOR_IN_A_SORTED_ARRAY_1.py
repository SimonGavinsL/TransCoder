#!/usr/bin/env python
""" generated source for module if__0__FLOOR_IN_A_SORTED_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def floorSearch(cls, arr, low, high, x):
        """ generated source for method floorSearch """
        if x >= arr[high]:
            return high
        mid = (low + high) / 2
        if arr[mid] == x:
            return mid
        if mid > 0 and arr[mid - 1] <= x and x < arr[mid]:
            return mid - 1
        if x < arr[mid]:
            return cls.floorSearch(arr, low, mid - 1, x)
        return cls.floorSearch(arr, mid + 1, high, x)

