#!/usr/bin/env python
""" generated source for module for__1__CHECK_POSSIBLE_TRANSFORM_ONE_STRING_ANOTHER """
class X(object):
    """ generated source for class X """
    @classmethod
    def check(cls, s1, s2):
        """ generated source for method check """
        n = len(s1)
        m = len(s2)
        dp = [None]*n + 1
        dp[0][0] = True
        return (dp[n][m])

