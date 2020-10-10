#!/usr/bin/env python
""" generated source for module for__0__FIND_N_TH_ELEMENT_FROM_STERNS_DIATOMIC_SERIES """
class X(object):
    """ generated source for class X """
    @classmethod
    def findSDSFunc(cls, n):
        """ generated source for method findSDSFunc """
        DP = [None]*n + 1
        DP[0] = 0
        DP[1] = 1
        return DP[n]

