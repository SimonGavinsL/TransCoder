#!/usr/bin/env python
""" generated source for module for__1__MINIMUM_CELLS_REQUIRED_REACH_DESTINATION_JUMPS_EQUAL_CELL_VALUES """
class X(object):
    """ generated source for class X """
    @classmethod
    def minCells(cls, mat, m, n):
        """ generated source for method minCells """
        dp = [None]*m
        dp[0][0] = 1
        if dp[m - 1][n - 1] != Integer.MAX_VALUE:
            return dp[m - 1][n - 1]
        return -1

