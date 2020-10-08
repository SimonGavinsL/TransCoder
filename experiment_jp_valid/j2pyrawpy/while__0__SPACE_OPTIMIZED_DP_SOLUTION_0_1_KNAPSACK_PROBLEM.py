#!/usr/bin/env python
""" generated source for module while__0__SPACE_OPTIMIZED_DP_SOLUTION_0_1_KNAPSACK_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def KnapSack(cls, val, wt, n, W):
        """ generated source for method KnapSack """
        mat = [None]*2
        i = 0
        return mat[0][W] if (n % 2 != 0) else mat[1][W]

