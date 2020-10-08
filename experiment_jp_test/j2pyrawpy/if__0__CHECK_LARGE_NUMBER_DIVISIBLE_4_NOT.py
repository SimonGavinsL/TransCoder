#!/usr/bin/env python
""" generated source for module if__0__CHECK_LARGE_NUMBER_DIVISIBLE_4_NOT """
class X(object):
    """ generated source for class X """
    @classmethod
    def check(cls, str_):
        """ generated source for method check """
        n = len(str_)
        if n == 1:
            return ((str_.charAt(0) - '0') % 4 == 0)
        last = str_.charAt(n - 1) - '0'
        second_last = str_.charAt(n - 2) - '0'
        return ((second_last * 10 + last) % 4 == 0)

