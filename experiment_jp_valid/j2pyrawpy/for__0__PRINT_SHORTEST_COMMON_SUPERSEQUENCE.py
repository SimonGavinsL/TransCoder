#!/usr/bin/env python
""" generated source for module for__0__PRINT_SHORTEST_COMMON_SUPERSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def printShortestSuperSeq(cls, X, Y):
        """ generated source for method printShortestSuperSeq """
        m = len(X)
        n = len(Y)
        dp = [None]*m + 1
        index = dp[m][n]
        str_ = " "
        i = m
        j = n
        while i > 0 and j > 0:
            if X.charAt(i - 1) == Y.charAt(j - 1):
                str_ += (X.charAt(i - 1))
                i -= 1
                j -= 1
                index -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                str_ += (Y.charAt(j - 1))
                j -= 1
                index -= 1
            else:
                str_ += (X.charAt(i - 1))
                i -= 1
                index -= 1
        while i > 0:
            str_ += (X.charAt(i - 1))
            i -= 1
            index -= 1
        while j > 0:
            str_ += (Y.charAt(j - 1))
            j -= 1
            index -= 1
        str_ = reverse(str_)
        return str_

