#!/usr/bin/env python
""" generated source for module if__0__NUMBER_DIGITS_PRODUCT_TWO_NUMBERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countDigits(cls, a, b):
        """ generated source for method countDigits """
        count = 0
        p = Math.abs(a * b)
        while p > 0:
            count += 1
            p = p / 10
        return count

