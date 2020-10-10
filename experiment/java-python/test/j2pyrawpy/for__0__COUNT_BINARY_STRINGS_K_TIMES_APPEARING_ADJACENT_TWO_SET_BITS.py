#!/usr/bin/env python
""" generated source for module for__0__COUNT_BINARY_STRINGS_K_TIMES_APPEARING_ADJACENT_TWO_SET_BITS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countStrings(cls, n, k):
        """ generated source for method countStrings """
        dp = [None]*n + 1
        dp[1][0][0] = 1
        dp[1][0][1] = 1
        return dp[n][k][0] + dp[n][k][1]

