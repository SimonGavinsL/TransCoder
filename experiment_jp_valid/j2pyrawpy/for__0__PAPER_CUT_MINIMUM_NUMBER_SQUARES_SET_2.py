#!/usr/bin/env python
""" generated source for module for__0__PAPER_CUT_MINIMUM_NUMBER_SQUARES_SET_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def minimumSquare(cls, m, n):
        """ generated source for method minimumSquare """
        vertical_min = Integer.MAX_VALUE
        horizontal_min = Integer.MAX_VALUE
        if m == n:
            return 1
        if dp[m][n] != 0:
            return dp[m][n]
        j = 1
        while j <= n / 2:
            vertical_min = Math.min(minimumSquare(m, j) + minimumSquare(m, n - j), vertical_min)
            j += 1
        dp[m][n] = Math.min(vertical_min, horizontal_min)
        return dp[m][n]

