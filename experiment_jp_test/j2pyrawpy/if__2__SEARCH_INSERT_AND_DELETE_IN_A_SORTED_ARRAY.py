#!/usr/bin/env python
""" generated source for module if__2__SEARCH_INSERT_AND_DELETE_IN_A_SORTED_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def binarySearch(cls, arr, low, high, key):
        """ generated source for method binarySearch """
        mid = (low + high) / 2
        return cls.binarySearch(arr, low, (mid - 1), key)

