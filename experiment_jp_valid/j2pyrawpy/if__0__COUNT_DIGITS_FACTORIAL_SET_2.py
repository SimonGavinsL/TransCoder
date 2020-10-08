#!/usr/bin/env python
""" generated source for module if__0__COUNT_DIGITS_FACTORIAL_SET_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findDigits(cls, n):
        """ generated source for method findDigits """
        if n <= 1:
            return 1
        x = (n * Math.log10(n / M_E) + Math.log10(2 * M_PI * n) / 2.0)
        return (Math.floor(x)) + 1

