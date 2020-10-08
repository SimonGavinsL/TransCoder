#!/usr/bin/env python
""" generated source for module for__0__RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def breakSum(cls, n):
        """ generated source for method breakSum """
        dp = [None]*n + 1
        dp[0] = 0
        dp[1] = 1
        return dp[n]

