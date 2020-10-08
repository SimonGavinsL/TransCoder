#!/usr/bin/env python
""" generated source for module for__0__LCS_FORMED_CONSECUTIVE_SEGMENTS_LEAST_LENGTH_K """
class X(object):
    """ generated source for class X """
    @classmethod
    def longestSubsequenceCommonSegment(cls, k, s1, s2):
        """ generated source for method longestSubsequenceCommonSegment """
        n = len(s1)
        m = len(s2)
        lcs = [None]*n + 1
        cnt = [None]*n + 1
        return lcs[n][m]

