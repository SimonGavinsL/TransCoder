#!/usr/bin/env python
""" generated source for module for__0__COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def numberOfPaths(cls, m, n):
        """ generated source for method numberOfPaths """
        dp = [None]*n
        dp[0] = 1
        return dp[n - 1]

