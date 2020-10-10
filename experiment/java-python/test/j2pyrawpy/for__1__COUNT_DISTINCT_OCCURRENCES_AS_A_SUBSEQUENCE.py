#!/usr/bin/env python
""" generated source for module for__1__COUNT_DISTINCT_OCCURRENCES_AS_A_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def findSubsequenceCount(cls, S, T):
        """ generated source for method findSubsequenceCount """
        m = len(T)
        n = len(S)
        if m > n:
            return 0
        mat = [None]*m + 1
        i = 1
        while i <= m:
            while j <= n:
                if T.charAt(i - 1) != S.charAt(j - 1):
                    mat[i][j] = mat[i][j - 1]
                else:
                    mat[i][j] = mat[i][j - 1] + mat[i - 1][j - 1]
                j += 1
            i += 1
        return mat[m][n]

