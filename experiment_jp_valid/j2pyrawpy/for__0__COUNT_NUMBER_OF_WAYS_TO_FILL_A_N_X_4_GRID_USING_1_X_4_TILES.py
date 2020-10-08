#!/usr/bin/env python
""" generated source for module for__0__COUNT_NUMBER_OF_WAYS_TO_FILL_A_N_X_4_GRID_USING_1_X_4_TILES """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, n):
        """ generated source for method count """
        dp = [None]*n + 1
        dp[0] = 0
        return dp[n]

