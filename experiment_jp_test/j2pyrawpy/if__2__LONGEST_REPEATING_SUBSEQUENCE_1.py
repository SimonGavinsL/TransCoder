#!/usr/bin/env python
""" generated source for module if__2__LONGEST_REPEATING_SUBSEQUENCE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findLongestRepeatingSubSeq(cls, X, m, n):
        """ generated source for method findLongestRepeatingSubSeq """
        return dp[m][n] = Math.max(findLongestRepeatingSubSeq(X, m, n - 1), findLongestRepeatingSubSeq(X, m - 1, n))

