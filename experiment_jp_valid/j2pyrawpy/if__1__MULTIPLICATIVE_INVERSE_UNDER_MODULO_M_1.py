#!/usr/bin/env python
""" generated source for module if__1__MULTIPLICATIVE_INVERSE_UNDER_MODULO_M_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def modInverse(cls, a, m):
        """ generated source for method modInverse """
        m0 = m
        y = 0
        x = 1
        while a > 1:
            m = a % m
            a = t
            t = y
            y = x - q * y
            x = t
        return x

