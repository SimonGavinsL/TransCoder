#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_NUMBER_OF_SQUARES_WHOSE_SUM_EQUALS_TO_GIVEN_NUMBER_N_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def getMinSquares(cls, n):
        """ generated source for method getMinSquares """
        if n <= 3:
            return n
        dp = [None]*n + 1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        res = dp[n]
        return res

