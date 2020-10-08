#!/usr/bin/env python
""" generated source for module for__2__COUNT_NUMBER_OF_WAYS_TO_PARTITION_A_SET_INTO_K_SUBSETS_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countP(cls, n, k):
        """ generated source for method countP """
        dp = [None]*n + 1
        return dp[n][k]

