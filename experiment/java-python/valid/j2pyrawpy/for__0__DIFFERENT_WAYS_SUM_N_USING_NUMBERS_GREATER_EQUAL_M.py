#!/usr/bin/env python
""" generated source for module for__0__DIFFERENT_WAYS_SUM_N_USING_NUMBERS_GREATER_EQUAL_M """
class X(object):
    """ generated source for class X """
    @classmethod
    def numberofways(cls, n, m):
        """ generated source for method numberofways """
        dp = [None]*n + 2
        dp[0][n + 1] = 1
        return dp[n][m]

