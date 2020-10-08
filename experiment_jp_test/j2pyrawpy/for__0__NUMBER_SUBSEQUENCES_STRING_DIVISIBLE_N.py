#!/usr/bin/env python
""" generated source for module for__0__NUMBER_SUBSEQUENCES_STRING_DIVISIBLE_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def countDivisibleSubseq(cls, str_, n):
        """ generated source for method countDivisibleSubseq """
        len = len(str_)
        dp = [None]*len
        dp[0][(str_.charAt(0) - '0') % n] += 1
        return dp[len - 1][0]

