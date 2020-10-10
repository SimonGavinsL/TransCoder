#!/usr/bin/env python
""" generated source for module do__0__STEINS_ALGORITHM_FOR_FINDING_GCD """
class X(object):
    """ generated source for class X """
    @classmethod
    def gcd(cls, a, b):
        """ generated source for method gcd """
        if a == 0:
            return b
        if b == 0:
            return a
        k = int()
        while ((a | b) & 1) == 0:
            a >>= 1
            b >>= 1
            k += 1
        while (a & 1) == 0:
        return a << k

