#!/usr/bin/env python
""" generated source for module for__2__COUNT_DISTINCT_OCCURRENCES_AS_A_SUBSEQUENCE """
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
        return mat[m][n]

