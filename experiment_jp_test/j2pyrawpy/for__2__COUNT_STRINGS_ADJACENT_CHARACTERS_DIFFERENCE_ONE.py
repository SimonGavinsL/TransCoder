#!/usr/bin/env python
""" generated source for module for__2__COUNT_STRINGS_ADJACENT_CHARACTERS_DIFFERENCE_ONE """
class X(object):
    """ generated source for class X """
    @classmethod
    def countStrs(cls, n):
        """ generated source for method countStrs """
        dp = [None]*n + 1
        sum = 0
        i = 0
        while i <= 25:
            sum = (sum + dp[n][i])
            i += 1
        return sum

