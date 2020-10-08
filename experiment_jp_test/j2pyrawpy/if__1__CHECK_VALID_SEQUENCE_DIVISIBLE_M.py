#!/usr/bin/env python
""" generated source for module if__1__CHECK_VALID_SEQUENCE_DIVISIBLE_M """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPossible(cls, n, index, sum, M, arr, dp):
        """ generated source for method isPossible """
        placeAdd = cls.isPossible(n, index + 1, sum + arr[index], M, arr, dp)
        placeMinus = cls.isPossible(n, index + 1, sum - arr[index], M, arr, dp)
        res = (placeAdd or placeMinus)
        dp[index][sum] = 1 if (res) else 0
        return res

