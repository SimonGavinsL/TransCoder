#!/usr/bin/env python
""" generated source for module if__4__FLOOR_IN_A_SORTED_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def floorSearch(cls, arr, low, high, x):
        """ generated source for method floorSearch """
        mid = (low + high) / 2
        return cls.floorSearch(arr, mid + 1, high, x)

