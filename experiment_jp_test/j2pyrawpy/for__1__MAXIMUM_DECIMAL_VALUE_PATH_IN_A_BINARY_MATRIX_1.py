#!/usr/bin/env python
""" generated source for module for__1__MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def MaximumDecimalValue(cls, mat, n):
        """ generated source for method MaximumDecimalValue """
        dp = [None]*n
        if mat[0][0] == 1:
            dp[0][0] = 1
        i = 1
        while i < n:
            while j < n:
                if mat[i][j] == 1:
                    dp[i][j] = ((Math.max(dp[i][j - 1], dp[i - 1][j]) + Math.pow(2, i + j)))
                else:
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j])
                j += 1
            i += 1
        return dp[n - 1][n - 1]

