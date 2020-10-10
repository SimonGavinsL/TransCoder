#!/usr/bin/env python
""" generated source for module if__3__SEARCH_AN_ELEMENT_IN_A_SORTED_AND_PIVOTED_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def search(cls, arr, l, h, key):
        """ generated source for method search """
        mid = (l + h) / 2
        return cls.search(arr, l, mid - 1, key)

