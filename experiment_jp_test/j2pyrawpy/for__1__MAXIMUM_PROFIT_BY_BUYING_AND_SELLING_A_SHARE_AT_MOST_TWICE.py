#!/usr/bin/env python
""" generated source for module for__1__MAXIMUM_PROFIT_BY_BUYING_AND_SELLING_A_SHARE_AT_MOST_TWICE """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxProfit(cls, price, n):
        """ generated source for method maxProfit """
        profit = [None]*n
        max_price = price[n - 1]
        min_price = price[0]
        i = 1
        while i < n:
            if price[i] < min_price:
                min_price = price[i]
            profit[i] = Math.max(profit[i - 1], profit[i] + (price[i] - min_price))
            i += 1
        result = profit[n - 1]
        return result

