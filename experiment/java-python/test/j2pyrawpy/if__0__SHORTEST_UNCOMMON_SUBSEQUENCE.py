#!/usr/bin/env python
""" generated source for module if__0__SHORTEST_UNCOMMON_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def shortestSeq(cls, S, T):
        """ generated source for method shortestSeq """
        m = S.length
        n = T.length
        dp = [None]*m + 1
        ans = dp[m][n]
        return ans

