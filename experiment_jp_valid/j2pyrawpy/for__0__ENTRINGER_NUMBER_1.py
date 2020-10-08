#!/usr/bin/env python
""" generated source for module for__0__ENTRINGER_NUMBER_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def zigzag(cls, n, k):
        """ generated source for method zigzag """
        dp = [None]*n + 1
        dp[0][0] = 1
        i = 1
        while i <= n:
            while j <= Math.min(i, k):
                j += 1
            i += 1
        return dp[n][k]

