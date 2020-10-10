#!/usr/bin/env python
""" generated source for module for__2__COUNT_ARRAYS_ADJACENT_ELEMENTS_ONE_DIVIDE_ANOTHER """
class X(object):
    """ generated source for class X """
    @classmethod
    def numofArray(cls, n, m):
        """ generated source for method numofArray """
        dp = [None]*MAX
        di = [None]*MAX
        mu = [None]*MAX
        i = 1
        while i <= m:
            i += 1
        i = 2
        while i <= n:
            while j <= m:
                dp[i][j] = 0
                for x in di[j]:
                    dp[i][j] += dp[i - 1][x]
                for x in mu[j]:
                    dp[i][j] += dp[i - 1][x]
                j += 1
            i += 1
        ans = 0
        i = 1
        while i <= m:
            ans += dp[n][i]
            di[i].clear()
            mu[i].clear()
            i += 1
        return ans

