#!/usr/bin/env python
""" generated source for module if__0__WAYS_TRANSFORMING_ONE_STRING_REMOVING_0_CHARACTERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countTransformation(cls, a, b):
        """ generated source for method countTransformation """
        n = len(a)
        m = len(b)
        dp = [None]*m + 1
        return dp[m - 1][n - 1]

