#!/usr/bin/env python
""" generated source for module if__1__FIND_MINIMUM_NUMBER_DIVIDED_MAKE_NUMBER_PERFECT_SQUARE """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMinNumber(cls, n):
        """ generated source for method findMinNumber """
        count = 0
        ans = 1
        while n % 2 == 0:
            count += 1
            n /= 2
        return ans

