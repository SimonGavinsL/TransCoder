#!/usr/bin/env python
""" generated source for module for__0__COUNT_OFDIFFERENT_WAYS_EXPRESS_N_SUM_1_3_4 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countWays(cls, n):
        """ generated source for method countWays """
        DP = [None]*n + 1
        DP[0] = DP[1] = DP[2] = 1
        DP[3] = 2
        return DP[n]

