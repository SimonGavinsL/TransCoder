#!/usr/bin/env python
""" generated source for module if__0__PROGRAM_FIND_GCD_FLOATING_POINT_NUMBERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def gcd(cls, a, b):
        """ generated source for method gcd """
        if Math.abs(b) < 0.001:
            return a
        else:
            return (cls.gcd(b, a - Math.floor(a / b) * b))

