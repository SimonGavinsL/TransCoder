#!/usr/bin/env python
""" generated source for module if__0__CHECK_VALID_SEQUENCE_DIVISIBLE_M_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPossible(cls, n, index, modulo, M, arr, dp):
        """ generated source for method isPossible """
        modulo = ((modulo % M) + M) % M
        if dp[index][modulo] != -1:
            return dp[index][modulo]
        placeAdd = cls.isPossible(n, index + 1, modulo + arr[index], M, arr, dp)
        placeMinus = cls.isPossible(n, index + 1, modulo - arr[index], M, arr, dp)
        res = placeAdd
        dp[index][modulo] = res
        return res

