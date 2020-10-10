#!/usr/bin/env python
""" generated source for module for__0__MINIMAL_MOVES_FORM_STRING_ADDING_CHARACTERS_APPENDING_STRING """
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
        i = 1
        while i < n:
            s1 += s.charAt(i)
            s2 = s.substring(i + 1, i + 1)
            dp[i] = Math.min(dp[i], dp[i - 1] + 1)
            if s1 == s2:
                dp[i * 2 + 1] = Math.min(dp[i] + 1, dp[i * 2 + 1])
            i += 1
        return dp[n - 1]

