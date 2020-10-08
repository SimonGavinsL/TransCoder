#!/usr/bin/env python
""" generated source for module for__0__LONGEST_CONSECUTIVE_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def findLongestConseqSubseq(cls, arr, n):
        """ generated source for method findLongestConseqSubseq """
        S = HashSet()
        ans = 0
        i = 0
        while i < n:
            if not S.contains(arr[i] - 1):
                while S.contains(j):
                if ans < j - arr[i]:
                    ans = j - arr[i]
            i += 1
        return ans

