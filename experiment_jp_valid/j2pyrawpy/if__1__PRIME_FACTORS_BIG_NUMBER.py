#!/usr/bin/env python
""" generated source for module if__1__PRIME_FACTORS_BIG_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def factorize(cls, n):
        """ generated source for method factorize """
        count = 0
        while not (n % 2 > 0):
            n >>= 1
            count += 1

