#!/usr/bin/env python
""" generated source for module for__1__MODULAR_MULTIPLICATIVE_INVERSE_1_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def modularInverse(cls, n, prime):
        """ generated source for method modularInverse """
        dp = [None]*n + 1
        dp[0] = dp[1] = 1

