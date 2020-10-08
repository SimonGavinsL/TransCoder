#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_STEPS_TO_DELETE_A_STRING_AFTER_REPEATED_DELETION_OF_PALINDROME_SUBSTRINGS """
class X(object):
    """ generated source for class X """
    @classmethod
    def minStepToDeleteString(cls, str_):
        """ generated source for method minStepToDeleteString """
        N = len(str_)
        dp = [None]*N + 1
        len = 1
        while len <= N:
            while j < N:
                if len == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + dp[i + 1][j]
                    if str_.charAt(i) == str_.charAt(i + 1):
                        dp[i][j] = Math.min(1 + dp[i + 2][j], dp[i][j])
                    while K <= j:
                        K += 1
                j += 1
            len += 1
        return dp[0][N - 1]

