#!/usr/bin/env python
""" generated source for module if__1__FIND_REPEATING_ELEMENT_SORTED_ARRAY_SIZE_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def findRepeatingElement(cls, arr, low, high):
        """ generated source for method findRepeatingElement """
        mid = (low + high) / 2
        return cls.findRepeatingElement(arr, mid + 1, high)

