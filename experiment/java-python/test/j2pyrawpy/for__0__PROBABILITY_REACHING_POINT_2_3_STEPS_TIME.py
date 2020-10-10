#!/usr/bin/env python
""" generated source for module for__0__PROBABILITY_REACHING_POINT_2_3_STEPS_TIME """
class X(object):
    """ generated source for class X """
    @classmethod
    def find_prob(cls, N, P):
        """ generated source for method find_prob """
        dp = [None]*N + 1
        dp[0] = 1
        dp[1] = 0
        dp[2] = P
        dp[3] = 1 - P
        return (((dp[N])))

