#!/usr/bin/env python
""" generated source for module for__0__BALANCED_EXPRESSIONS_SUCH_THAT_GIVEN_POSITIONS_HAVE_OPENING_BRACKETS """
class X(object):
    """ generated source for class X """
    @classmethod
    def arrangeBraces(cls, n, pos, k):
        """ generated source for method arrangeBraces """
        h = [None]*N
        dp = [None]*N
        dp[0][0] = 1
        i = 1
        while i <= 2 * n:
            while j <= 2 * n:
                if h[i]:
                    if j != 0:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 0
                elif j != 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i - 1][j + 1]
                j += 1
            i += 1
        return dp[2 * n][0]

