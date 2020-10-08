#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_COST_TO_FILL_GIVEN_WEIGHT_IN_A_BAG """
class X(object):
    """ generated source for class X """
    @classmethod
    def MinimumCost(cls, cost, n, W):
        """ generated source for method MinimumCost """
        val = Vector()
        wt = Vector()
        size = 0
        n = size
        min_cost = [None]*n + 1
        i = 0
        while i <= W:
            i += 1
        i = 1
        while i <= n:
            i += 1
        i = 1
        while i <= n:
            while j <= W:
                if wt.get(i - 1) > j:
                    min_cost[i][j] = min_cost[i - 1][j]
                else:
                    min_cost[i][j] = Math.min(min_cost[i - 1][j], min_cost[i][j - wt.get(i - 1)] + val.get(i - 1))
                j += 1
            i += 1
        return -1 if (min_cost[n][W] == Integer.MAX_VALUE) else min_cost[n][W]

