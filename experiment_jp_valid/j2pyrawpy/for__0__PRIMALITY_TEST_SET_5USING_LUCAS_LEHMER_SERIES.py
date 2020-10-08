#!/usr/bin/env python
""" generated source for module for__0__PRIMALITY_TEST_SET_5USING_LUCAS_LEHMER_SERIES """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPrime(cls, p):
        """ generated source for method isPrime """
        checkNumber = Math.pow(2, p) - 1
        nextval = 4 % checkNumber
        return (nextval == 0)

