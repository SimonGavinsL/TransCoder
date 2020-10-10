#!/usr/bin/env python
""" generated source for module for__0__MODIFY_ARRAY_TO_MAXIMIZE_SUM_OF_ADJACENT_DIFFERENCES """
class X(object):
    """ generated source for class X """
    @classmethod
    def maximumDifferenceSum(cls, arr, N):
        """ generated source for method maximumDifferenceSum """
        dp = [None]*N
        i = 0
        while i < (N - 1):
            dp[i + 1][0] = Math.max(dp[i][0], dp[i][1] + Math.abs(1 - arr[i]))
            dp[i + 1][1] = Math.max(dp[i][0] + Math.abs(arr[i + 1] - 1), dp[i][1] + Math.abs(arr[i + 1] - arr[i]))
            i += 1
        return Math.max(dp[N - 1][0], dp[N - 1][1])

