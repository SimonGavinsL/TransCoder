#!/usr/bin/env python
""" generated source for module for__2__SHORTEST_UNCOMMON_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def shortestSeq(cls, S, T):
        """ generated source for method shortestSeq """
        m = S.length
        n = T.length
        dp = [None]*m + 1
        ans = dp[m][n]
        if ans >= MAX:
            ans = -1
        return ans

