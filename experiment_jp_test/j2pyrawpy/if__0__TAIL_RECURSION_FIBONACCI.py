#!/usr/bin/env python
""" generated source for module if__0__TAIL_RECURSION_FIBONACCI """
class X(object):
    """ generated source for class X """
    @classmethod
    def fib(cls, n, a, b):
        """ generated source for method fib """
        if n == 1:
            return b
        return cls.fib(n - 1, b, a + b)

