#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_CONSECUTIVE_NUMBERS_PRESENT_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def findLongestConseqSubseq(cls, arr, n):
        """ generated source for method findLongestConseqSubseq """
        S = HashSet()
        ans = 0
        i = 0
        while i < n:
            if S.contains(arr[i]):
                while S.contains(j):
                ans = Math.max(ans, j - arr[i])
            i += 1
        return ans

