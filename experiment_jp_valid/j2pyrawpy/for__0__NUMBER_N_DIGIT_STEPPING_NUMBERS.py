#!/usr/bin/env python
""" generated source for module for__0__NUMBER_N_DIGIT_STEPPING_NUMBERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def answer(cls, n):
        """ generated source for method answer """
        dp = [None]*n + 1
        if n == 1:
            return 10
        i = 2
        while i <= n:
            while j <= 9:
                if j == 0:
                    dp[i][j] = dp[i - 1][j + 1]
                elif j == 9:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
                j += 1
            i += 1
        sum = 0
        j = 1
        while j <= 9:
            j += 1
        return sum

