#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_NUMBER_DELETIONS_MAKE_STRING_PALINDROME_SET_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def getLevenstein(cls, input):
        """ generated source for method getLevenstein """
        revInput = StringBuilder(input)
        revInput = revInput.reverse()
        n = len(input)
        dp = [None]*n + 1
        i = 1
        while i <= n:
            while j <= n:
                if input.charAt(i - 1) == revInput.charAt(j - 1):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1])
                j += 1
            i += 1
        res = Integer.MAX_VALUE
        i = n
        j = 0
        while i >= 0:
            res = Math.min(res, dp[i][j])
            if i < n:
                res = Math.min(res, dp[i + 1][j])
            if i > 0:
                res = Math.min(res, dp[i - 1][j])
            j += 1
        return res

