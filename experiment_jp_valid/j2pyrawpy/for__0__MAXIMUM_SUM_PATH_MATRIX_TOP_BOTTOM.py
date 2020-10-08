#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_SUM_PATH_MATRIX_TOP_BOTTOM """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxSum(cls, mat, n):
        """ generated source for method maxSum """
        if n == 1:
            return mat[0][0]
        dp = [None]*n
        maxSum = Integer.MIN_VALUE
        max = int()
        i = n - 2
        while i >= 0:
            while j < n:
                max = Integer.MIN_VALUE
                if ((j - 1) >= 0) and (max < dp[i + 1][j - 1]):
                    max = dp[i + 1][j - 1]
                if ((j + 1) < n) and (max < dp[i + 1][j + 1]):
                    max = dp[i + 1][j + 1]
                dp[i][j] = mat[i][j] + max
                j += 1
            i -= 1
        j = 0
        while j < n:
            j += 1
        return maxSum

