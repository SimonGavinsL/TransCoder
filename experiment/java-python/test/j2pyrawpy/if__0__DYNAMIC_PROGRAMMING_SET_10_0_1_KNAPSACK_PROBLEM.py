#!/usr/bin/env python
""" generated source for module if__0__DYNAMIC_PROGRAMMING_SET_10_0_1_KNAPSACK_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def knapSack(cls, W, wt, val, n):
        """ generated source for method knapSack """
        if wt[n - 1] > W:
            return cls.knapSack(W, wt, val, n - 1)
        else:
            return max(val[n - 1] + cls.knapSack(W - wt[n - 1], wt, val, n - 1), cls.knapSack(W, wt, val, n - 1))

