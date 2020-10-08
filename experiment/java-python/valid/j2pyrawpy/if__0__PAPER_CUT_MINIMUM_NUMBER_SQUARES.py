#!/usr/bin/env python
""" generated source for module if__0__PAPER_CUT_MINIMUM_NUMBER_SQUARES """
class X(object):
    """ generated source for class X """
    @classmethod
    def minimumSquare(cls, a, b):
        """ generated source for method minimumSquare """
        result = 0
        rem = 0
        while b > 0:
            result += a / b
            rem = a % b
            a = b
            b = rem
        return result

