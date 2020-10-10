#!/usr/bin/env python
""" generated source for module if__3__FIND_THE_MAXIMUM_ELEMENT_IN_AN_ARRAY_WHICH_IS_FIRST_INCREASING_AND_THEN_DECREASING_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMaximum(cls, arr, low, high):
        """ generated source for method findMaximum """
        mid = (low + high) / 2
        if arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
            return cls.findMaximum(arr, low, mid - 1)
        else:
            return cls.findMaximum(arr, mid + 1, high)

