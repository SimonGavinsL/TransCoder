#!/usr/bin/env python
""" generated source for module if__2__FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countRotations(cls, arr, low, high):
        """ generated source for method countRotations """
        mid = low + (high - low) / 2
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid
        if arr[high] > arr[mid]:
            return cls.countRotations(arr, low, mid - 1)
        return cls.countRotations(arr, mid + 1, high)

