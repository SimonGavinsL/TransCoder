#!/usr/bin/env python
""" generated source for module for__0__CHECK_POSSIBLE_TRANSFORM_ONE_STRING_ANOTHER """
class X(object):
    """ generated source for class X """
    @classmethod
    def check(cls, s1, s2):
        """ generated source for method check """
        n = len(s1)
        m = len(s2)
        dp = [None]*n + 1
        dp[0][0] = True
        i = 0
        while i < len(s1):
            while j <= len(s2):
                if dp[i][j]:
                    if j < len(s2) and (Character.toUpperCase(s1.charAt(i)) == s2.charAt(j)):
                        dp[i + 1][j + 1] = True
                    if not Character.isUpperCase(s1.charAt(i)):
                        dp[i + 1][j] = True
                j += 1
            i += 1
        return (dp[n][m])

