#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_SUM_SUBSEQUENCE_LEAST_ONE_EVERY_FOUR_CONSECUTIVE_ELEMENTS_PICKED """
class X(object):
    """ generated source for class X """
    @classmethod
    def minSum(cls, arr, n):
        """ generated source for method minSum """
        dp = [None]*n
        if n == 1:
            return arr[0]
        if n == 2:
            return Math.min(arr[0], arr[1])
        if n == 3:
            return Math.min(arr[0], Math.min(arr[1], arr[2]))
        if n == 4:
            return Math.min(Math.min(arr[0], arr[1]), Math.min(arr[2], arr[3]))
        dp[0] = arr[0]
        dp[1] = arr[1]
        dp[2] = arr[2]
        dp[3] = arr[3]
        return Math.min(Math.min(dp[n - 1], dp[n - 2]), Math.min(dp[n - 4], dp[n - 3]))

