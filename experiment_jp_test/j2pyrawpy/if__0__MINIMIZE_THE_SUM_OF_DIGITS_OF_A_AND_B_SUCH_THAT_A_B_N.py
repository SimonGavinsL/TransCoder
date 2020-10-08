#!/usr/bin/env python
""" generated source for module if__0__MINIMIZE_THE_SUM_OF_DIGITS_OF_A_AND_B_SUCH_THAT_A_B_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def minSum(cls, n):
        """ generated source for method minSum """
        sum = 0
        while n > 0:
            sum += (n % 10)
            n /= 10
        return sum

