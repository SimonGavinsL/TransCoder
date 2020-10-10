#!/usr/bin/env python
""" generated source for module if__0__LCS_LONGEST_COMMON_SUBSEQUENCE_THREE_STRINGS_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def lcsOf3(cls, i, j, k):
        """ generated source for method lcsOf3 """
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        if X.charAt(i) == Y.charAt(j) and Y.charAt(j) == Z.charAt(k):
            return dp[i][j][k] = 1 + lcsOf3(i - 1, j - 1, k - 1)
        else:
            return dp[i][j][k] = Math.max(Math.max(lcsOf3(i - 1, j, k), lcsOf3(i, j - 1, k)), lcsOf3(i, j, k - 1))

