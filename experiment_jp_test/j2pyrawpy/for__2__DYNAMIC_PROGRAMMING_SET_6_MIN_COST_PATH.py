#!/usr/bin/env python
""" generated source for module for__2__DYNAMIC_PROGRAMMING_SET_6_MIN_COST_PATH """
class X(object):
    """ generated source for class X """
    @classmethod
    def minCost(cls, cost, m, n):
        """ generated source for method minCost """
        i = int()
        j = int()
        tc = [None]*m + 1
        tc[0][0] = cost[0][0]
        return tc[m][n]

