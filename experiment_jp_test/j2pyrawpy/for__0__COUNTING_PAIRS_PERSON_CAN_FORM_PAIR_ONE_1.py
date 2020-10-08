#!/usr/bin/env python
""" generated source for module for__0__COUNTING_PAIRS_PERSON_CAN_FORM_PAIR_ONE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def numberOfWays(cls, x):
        """ generated source for method numberOfWays """
        dp = [None]*x + 1
        dp[0] = dp[1] = 1
        return dp[x]

