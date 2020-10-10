#!/usr/bin/env python
""" generated source for module for__2__MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def MaximumDecimalValue(cls, mat, n):
        """ generated source for method MaximumDecimalValue """
        dp = [None]*n
        if mat[0][0] == 1:
            dp[0][0] = 1
        return dp[n - 1][n - 1]

