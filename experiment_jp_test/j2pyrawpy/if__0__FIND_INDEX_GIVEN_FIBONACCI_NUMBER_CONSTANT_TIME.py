#!/usr/bin/env python
""" generated source for module if__0__FIND_INDEX_GIVEN_FIBONACCI_NUMBER_CONSTANT_TIME """
class X(object):
    """ generated source for class X """
    @classmethod
    def findIndex(cls, n):
        """ generated source for method findIndex """
        a = 0
        b = 1
        c = 1
        res = 1
        while c < n:
            c = a + b
            res += 1
            a = b
            b = c
        return res

