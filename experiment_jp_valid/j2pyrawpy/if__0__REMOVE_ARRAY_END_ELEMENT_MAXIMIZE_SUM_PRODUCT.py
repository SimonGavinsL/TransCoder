#!/usr/bin/env python
""" generated source for module if__0__REMOVE_ARRAY_END_ELEMENT_MAXIMIZE_SUM_PRODUCT """
class X(object):
    """ generated source for class X """
    @classmethod
    def solve(cls, dp, a, low, high, turn):
        """ generated source for method solve """
        if dp[low][high] != 0:
            return dp[low][high]
        dp[low][high] = Math.max(a[low] * turn + solve(dp, a, low + 1, high, turn + 1), a[high] * turn + solve(dp, a, low, high - 1, turn + 1))
        return dp[low][high]

