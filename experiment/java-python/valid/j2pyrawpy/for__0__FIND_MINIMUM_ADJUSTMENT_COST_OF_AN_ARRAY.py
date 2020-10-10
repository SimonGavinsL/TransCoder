#!/usr/bin/env python
""" generated source for module for__0__FIND_MINIMUM_ADJUSTMENT_COST_OF_AN_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def minAdjustmentCost(cls, A, n, target):
        """ generated source for method minAdjustmentCost """
        dp = [None]*n
        i = 1
        while i < n:
            while j <= M:
                dp[i][j] = Integer.MAX_VALUE
                while k <= Math.min(M, j + target):
                    k += 1
                j += 1
            i += 1
        res = Integer.MAX_VALUE
        j = 0
        while j <= M:
            j += 1
        return res

