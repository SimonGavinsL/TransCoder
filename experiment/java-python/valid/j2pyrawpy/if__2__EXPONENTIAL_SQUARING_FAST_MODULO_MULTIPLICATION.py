#!/usr/bin/env python
""" generated source for module if__2__EXPONENTIAL_SQUARING_FAST_MODULO_MULTIPLICATION """
class X(object):
    """ generated source for class X """
    @classmethod
    def exponentiation(cls, base, exp):
        """ generated source for method exponentiation """
        t = cls.exponentiation(base, exp / 2)
        t = (t * t) % N

