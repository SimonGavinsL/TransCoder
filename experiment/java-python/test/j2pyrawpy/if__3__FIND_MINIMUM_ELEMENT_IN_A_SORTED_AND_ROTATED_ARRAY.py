#!/usr/bin/env python
""" generated source for module if__3__FIND_MINIMUM_ELEMENT_IN_A_SORTED_AND_ROTATED_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMin(cls, arr, low, high):
        """ generated source for method findMin """
        mid = low + (high - low) / 2
        if arr[high] > arr[mid]:
            return cls.findMin(arr, low, mid - 1)
        return cls.findMin(arr, mid + 1, high)

