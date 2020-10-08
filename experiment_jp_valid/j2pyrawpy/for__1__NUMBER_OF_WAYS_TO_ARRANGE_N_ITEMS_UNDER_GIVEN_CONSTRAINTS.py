#!/usr/bin/env python
""" generated source for module for__1__NUMBER_OF_WAYS_TO_ARRANGE_N_ITEMS_UNDER_GIVEN_CONSTRAINTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def waysToArrange(cls, N, K, k):
        """ generated source for method waysToArrange """
        C = [None]*N + 1
        i = int()
        j = int()
        dp = [None]*K + 1
        count = 0
        dp[0] = 1
        return dp[K]

