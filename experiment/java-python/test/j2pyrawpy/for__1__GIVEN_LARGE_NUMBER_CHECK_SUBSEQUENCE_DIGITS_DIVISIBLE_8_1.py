#!/usr/bin/env python
""" generated source for module for__1__GIVEN_LARGE_NUMBER_CHECK_SUBSEQUENCE_DIGITS_DIVISIBLE_8_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isSubSeqDivisible(cls, str_):
        """ generated source for method isSubSeqDivisible """
        n = len(str_)
        dp = [None]*n + 1
        arr = [None]*n + 1
        i = 1
        while i <= n:
            if dp[i][0] == 1:
                return True
            i += 1
        return False

