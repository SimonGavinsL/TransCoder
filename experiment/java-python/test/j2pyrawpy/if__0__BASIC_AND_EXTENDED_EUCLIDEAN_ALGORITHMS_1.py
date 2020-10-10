#!/usr/bin/env python
""" generated source for module if__0__BASIC_AND_EXTENDED_EUCLIDEAN_ALGORITHMS_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def gcdExtended(cls, a, b, x, y):
        """ generated source for method gcdExtended """
        x1 = 1
        y1 = 1
        gcd = cls.gcdExtended(b % a, a, x1, y1)
        x = y1 - (b / a) * x1
        y = x1
        return gcd

