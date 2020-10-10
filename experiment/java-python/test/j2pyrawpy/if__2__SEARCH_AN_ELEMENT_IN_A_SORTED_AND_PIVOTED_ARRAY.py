#!/usr/bin/env python
""" generated source for module if__2__SEARCH_AN_ELEMENT_IN_A_SORTED_AND_PIVOTED_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def search(cls, arr, l, h, key):
        """ generated source for method search """
        mid = (l + h) / 2
        if key >= arr[mid] and key <= arr[h]:
            return cls.search(arr, mid + 1, h, key)
        return cls.search(arr, l, mid - 1, key)

