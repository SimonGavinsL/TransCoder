#!/usr/bin/env python
""" generated source for module for__0__NUMBER_SUBSTRINGS_DIVISIBLE_4_STRING_INTEGERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countDivisbleby4(cls, s):
        """ generated source for method countDivisbleby4 """
        n = len(s)
        count = 0
        i = 0
        while i < n - 1:
            if h % 4 == 0:
                count = count + i + 1
            i += 1
        return count

