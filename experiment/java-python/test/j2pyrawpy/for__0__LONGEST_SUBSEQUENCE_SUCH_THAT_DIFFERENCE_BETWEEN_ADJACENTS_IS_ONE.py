#!/usr/bin/env python
""" generated source for module for__0__LONGEST_SUBSEQUENCE_SUCH_THAT_DIFFERENCE_BETWEEN_ADJACENTS_IS_ONE """
class X(object):
    """ generated source for class X """
    @classmethod
    def longestSubseqWithDiffOne(cls, arr, n):
        """ generated source for method longestSubseqWithDiffOne """
        dp = [None]*n
        i = 1
        while i < n:
            while j < i:
                if (arr[i] == arr[j] + 1) or (arr[i] == arr[j] - 1):
                    dp[i] = Math.max(dp[i], dp[j] + 1)
                j += 1
            i += 1
        result = 1
        i = 0
        while i < n:
            i += 1
        return result

