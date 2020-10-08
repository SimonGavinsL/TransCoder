#!/usr/bin/env python
""" generated source for module if__1__LONGEST_REPEATING_SUBSEQUENCE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findLongestRepeatingSubSeq(cls, X, m, n):
        """ generated source for method findLongestRepeatingSubSeq """
        if X[m - 1] == X[n - 1] and m != n:
            return dp[m][n] = findLongestRepeatingSubSeq(X, m - 1, n - 1) + 1
        return dp[m][n] = Math.max(findLongestRepeatingSubSeq(X, m, n - 1), findLongestRepeatingSubSeq(X, m - 1, n))

