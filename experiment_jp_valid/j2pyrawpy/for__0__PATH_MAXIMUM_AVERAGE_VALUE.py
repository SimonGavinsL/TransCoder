#!/usr/bin/env python
""" generated source for module for__0__PATH_MAXIMUM_AVERAGE_VALUE """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxAverageOfPath(cls, cost, N):
        """ generated source for method maxAverageOfPath """
        dp = [None]*N + 1
        dp[0][0] = cost[0][0]
        j = 1
        while j < N:
            j += 1
        i = 1
        while i < N:
            i += 1
        return (dp[N - 1][N - 1]) / (2 * N - 1)

