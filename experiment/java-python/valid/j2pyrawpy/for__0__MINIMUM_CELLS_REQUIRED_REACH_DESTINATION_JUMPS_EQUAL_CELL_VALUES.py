#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_CELLS_REQUIRED_REACH_DESTINATION_JUMPS_EQUAL_CELL_VALUES """
class X(object):
    """ generated source for class X """
    @classmethod
    def minCells(cls, mat, m, n):
        """ generated source for method minCells """
        dp = [None]*m
        dp[0][0] = 1
        i = 0
        while i < m:
            while j < n:
                if dp[i][j] != Integer.MAX_VALUE and (j + mat[i][j]) < n and (dp[i][j] + 1) < dp[i][j + mat[i][j]]:
                    dp[i][j + mat[i][j]] = dp[i][j] + 1
                if dp[i][j] != Integer.MAX_VALUE and (i + mat[i][j]) < m and (dp[i][j] + 1) < dp[i + mat[i][j]][j]:
                    dp[i + mat[i][j]][j] = dp[i][j] + 1
                j += 1
            i += 1
        if dp[m - 1][n - 1] != Integer.MAX_VALUE:
            return dp[m - 1][n - 1]
        return -1

