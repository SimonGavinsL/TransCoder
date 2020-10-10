#!/usr/bin/env python
""" generated source for module while__0__NTH_NON_FIBONACCI_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def nonFibonacci(cls, n):
        """ generated source for method nonFibonacci """
        prevPrev = 1
        prev = 2
        curr = 3
        n = n + (curr - prev - 1)
        return prev + n

