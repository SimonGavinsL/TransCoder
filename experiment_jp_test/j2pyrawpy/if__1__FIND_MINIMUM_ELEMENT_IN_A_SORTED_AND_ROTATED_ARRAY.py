#!/usr/bin/env python
""" generated source for module if__1__FIND_MINIMUM_ELEMENT_IN_A_SORTED_AND_ROTATED_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMin(cls, arr, low, high):
        """ generated source for method findMin """
        mid = low + (high - low) / 2
        if mid < high and arr[mid + 1] < arr[mid]:
            return arr[mid + 1]
        if mid > low and arr[mid] < arr[mid - 1]:
            return arr[mid]
        if arr[high] > arr[mid]:
            return cls.findMin(arr, low, mid - 1)
        return cls.findMin(arr, mid + 1, high)

