#!/usr/bin/env python
""" generated source for module if__0__ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION """
class X(object):
    """ generated source for class X """
    @classmethod
    def nearestSmallerEqFib(cls, n):
        """ generated source for method nearestSmallerEqFib """
        f1 = 0
        f2 = 1
        f3 = 1
        while f3 <= n:
            f1 = f2
            f2 = f3
            f3 = f1 + f2
        return f2

