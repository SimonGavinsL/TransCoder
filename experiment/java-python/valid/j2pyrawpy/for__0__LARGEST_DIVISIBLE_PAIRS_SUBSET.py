#!/usr/bin/env python
""" generated source for module for__0__LARGEST_DIVISIBLE_PAIRS_SUBSET """
class X(object):
    """ generated source for class X """
    @classmethod
    def largestSubset(cls, a, n):
        """ generated source for method largestSubset """
        Arrays.sort(a)
        dp = [None]*n
        dp[n - 1] = 1
        return Arrays.stream(dp).max().getAsInt()

