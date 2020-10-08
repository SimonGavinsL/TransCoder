#!/usr/bin/env python
""" generated source for module if__0__PAPER_CUT_MINIMUM_NUMBER_SQUARES_SET_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def minimumSquare(cls, m, n):
        """ generated source for method minimumSquare """
        vertical_min = Integer.MAX_VALUE
        horizontal_min = Integer.MAX_VALUE
        if dp[m][n] != 0:
            return dp[m][n]
        dp[m][n] = Math.min(vertical_min, horizontal_min)
        return dp[m][n]

