#!/usr/bin/env python
""" generated source for module if__0__RECURSIVE_PROGRAM_PRIME_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPrime(cls, n, i):
        """ generated source for method isPrime """
        if n % i == 0:
            return False
        if i * i > n:
            return True
        return cls.isPrime(n, i + 1)

