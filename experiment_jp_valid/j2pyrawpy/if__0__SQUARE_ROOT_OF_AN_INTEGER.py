#!/usr/bin/env python
""" generated source for module if__0__SQUARE_ROOT_OF_AN_INTEGER """
class X(object):
    """ generated source for class X """
    @classmethod
    def floorSqrt(cls, x):
        """ generated source for method floorSqrt """
        i = 1
        result = 1
        while result <= x:
            i += 1
            result = i * i
        return i - 1

