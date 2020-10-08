#!/usr/bin/env python
""" generated source for module if__0__FIND_REPEATING_ELEMENT_SORTED_ARRAY_SIZE_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def findRepeatingElement(cls, arr, low, high):
        """ generated source for method findRepeatingElement """
        mid = (low + high) / 2
        if arr[mid] != mid + 1:
            if mid > 0 and arr[mid] == arr[mid - 1]:
                return mid
            return cls.findRepeatingElement(arr, low, mid - 1)
        return cls.findRepeatingElement(arr, mid + 1, high)

