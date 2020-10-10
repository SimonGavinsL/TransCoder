#!/usr/bin/env python
""" generated source for module for__1__SHORTEST_UNCOMMON_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def shortestSeq(cls, S, T):
        """ generated source for method shortestSeq """
        m = S.length
        n = T.length
        dp = [None]*m + 1
        i = 1
        while i <= m:
            while j <= n:
                while k >= 0:
                    if T[k] == ch:
                        break
                    k -= 1
                if k == -1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][k] + 1)
                j += 1
            i += 1
        ans = dp[m][n]
        if ans >= MAX:
            ans = -1
        return ans

