#!/usr/bin/env python
""" generated source for module for__0__MAXIMIZE_ARRAY_ELEMENTS_UPTO_GIVEN_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMaxVal(cls, arr, n, num, maxLimit):
        """ generated source for method findMaxVal """
        ind = int()
        val = int()
        dp = [None]*n
        while val >= 0:
            if dp[n - 1][val] == 1:
                return val
            val -= 1
        return -1

