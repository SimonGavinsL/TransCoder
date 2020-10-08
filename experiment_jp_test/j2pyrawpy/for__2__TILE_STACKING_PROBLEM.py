#!/usr/bin/env python
""" generated source for module for__2__TILE_STACKING_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def possibleWays(cls, n, m, k):
        """ generated source for method possibleWays """
        dp = [None]*N
        presum = [None]*N
        i = 1
        while i < m + 1:
            while j < n + 1:
                dp[i][j] = presum[i - 1][j]
                if j > k:
                    dp[i][j] -= presum[i - 1][j - k - 1]
                j += 1
            while j < n + 1:
                presum[i][j] = dp[i][j] + presum[i][j - 1]
                j += 1
            i += 1
        return dp[m][n]

