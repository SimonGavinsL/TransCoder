#!/usr/bin/env python
""" generated source for module for__0__PRIMALITY_TEST_SET_1_INTRODUCTION_AND_SCHOOL_METHOD_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPrime(cls, n):
        """ generated source for method isPrime """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        return True

