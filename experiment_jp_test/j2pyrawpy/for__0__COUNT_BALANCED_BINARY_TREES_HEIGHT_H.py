#!/usr/bin/env python
""" generated source for module for__0__COUNT_BALANCED_BINARY_TREES_HEIGHT_H """
class X(object):
    """ generated source for class X """
    @classmethod
    def countBT(cls, h):
        """ generated source for method countBT """
        dp = [None]*h + 1
        dp[0] = 1
        dp[1] = 1
        return dp[h]

