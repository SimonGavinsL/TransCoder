#!/usr/bin/env python
""" generated source for module for__0__LEONARDO_NUMBER_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def leonardo(cls, n):
        """ generated source for method leonardo """
        dp = [None]*n + 1
        dp[0] = dp[1] = 1
        return dp[n]

