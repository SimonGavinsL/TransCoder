#!/usr/bin/env python
""" generated source for module for__0__COUNT_STRINGS_ADJACENT_CHARACTERS_DIFFERENCE_ONE """
class X(object):
    """ generated source for class X """
    @classmethod
    def countStrs(cls, n):
        """ generated source for method countStrs """
        dp = [None]*n + 1
        i = 0
        while i <= 25:
            dp[1][i] = 1
            i += 1
        i = 2
        while i <= n:
            while j <= 25:
                if j == 0:
                    dp[i][j] = dp[i - 1][j + 1]
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1])
                j += 1
            i += 1
        sum = 0
        i = 0
        while i <= 25:
            sum = (sum + dp[n][i])
            i += 1
        return sum

