#!/usr/bin/env python
""" generated source for module if__1__SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def binarySearch(cls, arr, low, high, key):
        """ generated source for method binarySearch """
        mid = (low + high) / 2
        if key > arr[mid]:
            return cls.binarySearch(arr, (mid + 1), high, key)
        return cls.binarySearch(arr, low, (mid - 1), key)

