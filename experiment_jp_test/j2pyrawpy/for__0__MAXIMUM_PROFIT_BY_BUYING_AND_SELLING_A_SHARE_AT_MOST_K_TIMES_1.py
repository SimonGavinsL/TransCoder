#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_K_TIMES_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxProfit(cls, price, n, k):
        """ generated source for method maxProfit """
        profit = [None]*k + 1
        j = 0
        while j <= n:
            j += 1
        i = 1
        while i <= k:
            while j < n:
                prevDiff = Math.max(prevDiff, profit[i - 1][j - 1] - price[j - 1])
                profit[i][j] = Math.max(profit[i][j - 1], price[j] + prevDiff)
                j += 1
            i += 1
        return profit[k][n - 1]

