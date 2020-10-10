#!/usr/bin/env python
""" generated source for module if__0__RECURSIVE_C_PROGRAM_LINEARLY_SEARCH_ELEMENT_GIVEN_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def recSearch(cls, arr, l, r, x):
        """ generated source for method recSearch """
        if arr[l] == x:
            return l
        if arr[r] == x:
            return r
        return cls.recSearch(arr, l + 1, r - 1, x)

