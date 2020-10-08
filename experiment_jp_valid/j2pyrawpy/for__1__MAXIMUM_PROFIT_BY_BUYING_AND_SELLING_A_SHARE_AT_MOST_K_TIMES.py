#!/usr/bin/env python
""" generated source for module for__1__MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_K_TIMES """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxProfit(cls, price, n, k):
        """ generated source for method maxProfit """
        profit = [None]*k + 1
        i = 1
        while i <= k:
            while j < n:
                while m < j:
                    m += 1
                profit[i][j] = Math.max(profit[i][j - 1], max_so_far)
                j += 1
            i += 1
        return profit[k][n - 1]

