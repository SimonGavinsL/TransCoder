#!/usr/bin/env python
""" generated source for module if__2__COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countPS(cls, i, j):
        """ generated source for method countPS """
        if i == j:
            return dp[1][j] = 1
        elif str_.charAt(i) == str_.charAt(j):
            return dp[i][j] = countPS(i + 1, j) + countPS(i, j - 1) + 1
        else:
            return dp[i][j] = countPS(i + 1, j) + countPS(i, j - 1) - countPS(i + 1, j - 1)

