#!/usr/bin/env python
""" generated source for module for__1__COUNT_NUMBER_INCREASING_SUBSEQUENCES_SIZE_K """
class X(object):
    """ generated source for class X """
    @classmethod
    def numOfIncSubseqOfSizeK(cls, arr, n, k):
        """ generated source for method numOfIncSubseqOfSizeK """
        dp = [None]*k
        sum = 0
        i = k - 1
        while i < n:
            sum += dp[k - 1][i]
            i += 1
        return sum

