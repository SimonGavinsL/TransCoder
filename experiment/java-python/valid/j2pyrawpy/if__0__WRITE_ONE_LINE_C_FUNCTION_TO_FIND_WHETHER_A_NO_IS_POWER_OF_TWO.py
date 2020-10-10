#!/usr/bin/env python
""" generated source for module if__0__WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPowerOfTwo(cls, n):
        """ generated source for method isPowerOfTwo """
        while n != 1:
            if n % 2 != 0:
                return False
            n = n / 2
        return True

