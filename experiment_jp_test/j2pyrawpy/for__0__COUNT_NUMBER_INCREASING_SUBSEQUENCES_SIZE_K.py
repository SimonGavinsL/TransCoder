#!/usr/bin/env python
""" generated source for module for__0__COUNT_NUMBER_INCREASING_SUBSEQUENCES_SIZE_K """
class X(object):
    """ generated source for class X """
    @classmethod
    def numOfIncSubseqOfSizeK(cls, arr, n, k):
        """ generated source for method numOfIncSubseqOfSizeK """
        dp = [None]*k
        sum = 0
        l = 1
        while l < k:
            while i < n:
                dp[l][i] = 0
                while j < i:
                    if arr[j] < arr[i]:
                        dp[l][i] += dp[l - 1][j]
                    j += 1
                i += 1
            l += 1
        i = k - 1
        while i < n:
            sum += dp[k - 1][i]
            i += 1
        return sum

