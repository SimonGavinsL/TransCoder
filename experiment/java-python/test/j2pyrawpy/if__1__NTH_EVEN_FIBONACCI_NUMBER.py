#!/usr/bin/env python
""" generated source for module if__1__NTH_EVEN_FIBONACCI_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def evenFib(cls, n):
        """ generated source for method evenFib """
        return ((4 * cls.evenFib(n - 1)) + cls.evenFib(n - 2))

