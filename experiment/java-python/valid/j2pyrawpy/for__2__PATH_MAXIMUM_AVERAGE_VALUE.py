#!/usr/bin/env python
""" generated source for module for__2__PATH_MAXIMUM_AVERAGE_VALUE """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxAverageOfPath(cls, cost, N):
        """ generated source for method maxAverageOfPath """
        dp = [None]*N + 1
        dp[0][0] = cost[0][0]
        return (dp[N - 1][N - 1]) / (2 * N - 1)

