#!/usr/bin/env python
""" generated source for module for__0__COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countWays(cls, n):
        """ generated source for method countWays """
        dp = [None]*2
        dp[0][1] = 1
        dp[1][1] = 2
        return dp[0][n] + dp[1][n]

