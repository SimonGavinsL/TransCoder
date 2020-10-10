#!/usr/bin/env python
""" generated source for module for__0__FIND_LENGTH_LONGEST_SUBSEQUENCE_ONE_STRING_SUBSTRING_ANOTHER_STRING """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxSubsequenceSubstring(cls, x, y, n, m):
        """ generated source for method maxSubsequenceSubstring """
        dp = [None]*MAX
        i = 1
        while i <= m:
            while j <= n:
                if x[j - 1] == y[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
                j += 1
            i += 1
        ans = 0
        i = 1
        while i <= m:
            i += 1
        return ans

