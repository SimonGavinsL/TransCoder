#!/usr/bin/env python
""" generated source for module for__0__FIND_MINIMUM_NUMBER_DIVIDED_MAKE_NUMBER_PERFECT_SQUARE """
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
        if count % 2 == 1:
            ans *= 2
        if n > 2:
            ans *= n
        return ans

