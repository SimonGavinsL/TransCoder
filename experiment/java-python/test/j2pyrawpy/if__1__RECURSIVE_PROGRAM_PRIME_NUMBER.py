#!/usr/bin/env python
""" generated source for module if__1__RECURSIVE_PROGRAM_PRIME_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPrime(cls, n, i):
        """ generated source for method isPrime """
        if i * i > n:
            return True
        return cls.isPrime(n, i + 1)

