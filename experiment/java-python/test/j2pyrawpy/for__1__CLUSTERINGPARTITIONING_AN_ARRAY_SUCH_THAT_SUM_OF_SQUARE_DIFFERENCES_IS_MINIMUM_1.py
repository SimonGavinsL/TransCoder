#!/usr/bin/env python
""" generated source for module for__1__CLUSTERINGPARTITIONING_AN_ARRAY_SUCH_THAT_SUM_OF_SQUARE_DIFFERENCES_IS_MINIMUM_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def minCost(cls, a, n, k):
        """ generated source for method minCost """
        dp = [None]*n + 1
        dp[0][0] = 0
        return dp[n][k]

