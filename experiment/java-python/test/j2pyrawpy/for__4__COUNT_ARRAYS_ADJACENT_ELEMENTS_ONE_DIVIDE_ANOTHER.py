#!/usr/bin/env python
""" generated source for module for__4__COUNT_ARRAYS_ADJACENT_ELEMENTS_ONE_DIVIDE_ANOTHER """
class X(object):
    """ generated source for class X """
    @classmethod
    def numofArray(cls, n, m):
        """ generated source for method numofArray """
        dp = [None]*MAX
        di = [None]*MAX
        mu = [None]*MAX
        ans = 0
        i = 1
        while i <= m:
            ans += dp[n][i]
            di[i].clear()
            mu[i].clear()
            i += 1
        return ans

