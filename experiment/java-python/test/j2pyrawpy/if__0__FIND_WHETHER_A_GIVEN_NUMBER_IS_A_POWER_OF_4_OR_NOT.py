#!/usr/bin/env python
""" generated source for module if__0__FIND_WHETHER_A_GIVEN_NUMBER_IS_A_POWER_OF_4_OR_NOT """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPowerOfFour(cls, n):
        """ generated source for method isPowerOfFour """
        while n != 1:
            if n % 4 != 0:
                return 0
            n = n / 4
        return 1

