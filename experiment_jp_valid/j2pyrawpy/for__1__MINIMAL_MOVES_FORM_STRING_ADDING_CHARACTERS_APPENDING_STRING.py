#!/usr/bin/env python
""" generated source for module for__1__MINIMAL_MOVES_FORM_STRING_ADDING_CHARACTERS_APPENDING_STRING """
class X(object):
    """ generated source for class X """
    @classmethod
    def minimalSteps(cls, s, n):
        """ generated source for method minimalSteps """
        dp = [None]*n
        s1 = " "
        s2 = " "
        dp[0] = 1
        s1 += s.charAt(0)
        return dp[n - 1]

