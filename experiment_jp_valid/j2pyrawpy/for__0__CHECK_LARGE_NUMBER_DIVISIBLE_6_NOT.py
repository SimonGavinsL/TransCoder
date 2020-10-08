#!/usr/bin/env python
""" generated source for module for__0__CHECK_LARGE_NUMBER_DIVISIBLE_6_NOT """
class X(object):
    """ generated source for class X """
    @classmethod
    def check(cls, str_):
        """ generated source for method check """
        n = len(str_)
        if (str_.charAt(n - 1) - '0') % 2 != 0:
            return False
        digitSum = 0
        return (digitSum % 3 == 0)

