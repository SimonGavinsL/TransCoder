#!/usr/bin/env python
""" generated source for module for__2__MINIMUM_POSITIVE_POINTS_TO_REACH_DESTINATION """
class X(object):
    """ generated source for class X """
    @classmethod
    def minInitialPoints(cls, points, R, C):
        """ generated source for method minInitialPoints """
        dp = [None]*R
        m = R
        n = C
        dp[m - 1][n - 1] = 1 if points[m - 1][n - 1] > 0 else Math.abs(points[m - 1][n - 1]) + 1
        return dp[0][0]

