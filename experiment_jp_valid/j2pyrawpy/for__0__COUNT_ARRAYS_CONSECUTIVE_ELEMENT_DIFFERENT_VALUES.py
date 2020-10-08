#!/usr/bin/env python
""" generated source for module for__0__COUNT_ARRAYS_CONSECUTIVE_ELEMENT_DIFFERENT_VALUES """
class X(object):
    """ generated source for class X """
    @classmethod
    def countarray(cls, n, k, x):
        """ generated source for method countarray """
        dp = [None]*109
        dp[0] = 0
        dp[1] = 1
        return ((k - 1) * dp[n - 2] if x == 1 else dp[n - 1])

