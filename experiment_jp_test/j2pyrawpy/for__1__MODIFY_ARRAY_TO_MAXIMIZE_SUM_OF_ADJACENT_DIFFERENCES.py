#!/usr/bin/env python
""" generated source for module for__1__MODIFY_ARRAY_TO_MAXIMIZE_SUM_OF_ADJACENT_DIFFERENCES """
class X(object):
    """ generated source for class X """
    @classmethod
    def maximumDifferenceSum(cls, arr, N):
        """ generated source for method maximumDifferenceSum """
        dp = [None]*N
        return Math.max(dp[N - 1][0], dp[N - 1][1])

