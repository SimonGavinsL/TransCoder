#!/usr/bin/env python
""" generated source for module for__0__COUNT_PALINDROME_SUB_STRINGS_STRING """
class X(object):
    """ generated source for class X """
    @classmethod
    def CountPS(cls, str_, n):
        """ generated source for method CountPS """
        dp = [None]*n
        P = [None]*n
        i = 0
        while i < n - 1:
            if str_[i] == str_[i + 1]:
                P[i][i + 1] = True
                dp[i][i + 1] = 1
            i += 1
        gap = 2
        while gap < n:
            while i < n - gap:
                if str_[i] == str_[j] and P[i + 1][j - 1]:
                    P[i][j] = True
                if P[i][j] == True:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] + 1 - dp[i + 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
                i += 1
            gap += 1
        return dp[0][n - 1]

