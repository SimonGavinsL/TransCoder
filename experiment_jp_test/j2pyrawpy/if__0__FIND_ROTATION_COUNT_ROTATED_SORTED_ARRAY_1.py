#!/usr/bin/env python
""" generated source for module if__0__FIND_ROTATION_COUNT_ROTATED_SORTED_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countRotations(cls, arr, low, high):
        """ generated source for method countRotations """
        if high == low:
            return low
        mid = low + (high - low) / 2
        if mid < high and arr[mid + 1] < arr[mid]:
            return (mid + 1)
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid
        if arr[high] > arr[mid]:
            return cls.countRotations(arr, low, mid - 1)
        return cls.countRotations(arr, mid + 1, high)

