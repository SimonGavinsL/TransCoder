#!/usr/bin/env python
""" generated source for module for__1__LONGEST_REPEATED_SUBSEQUENCE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def longestRepeatedSubSeq(cls, str_):
        """ generated source for method longestRepeatedSubSeq """
        n = len(str_)
        dp = [None]*n + 1
        res = " "
        i = n
        j = n
        while i > 0 and j > 0:
            if dp[i][j] == dp[i - 1][j - 1] + 1:
                res = res + str_.charAt(i - 1)
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                j -= 1
        reverse = " "
        k = len(res) - 1
        while k >= 0:
            reverse = reverse + res.charAt(k)
            k -= 1
        return reverse

