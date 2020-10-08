#!/usr/bin/env python
""" generated source for module for__0__COUNT_DISTINCT_SUBSEQUENCES """
class X(object):
    """ generated source for class X """
    @classmethod
    def countSub(cls, str_):
        """ generated source for method countSub """
        last = [None]*MAX_CHAR
        Arrays.fill(last, -1)
        n = len(str_)
        dp = [None]*n + 1
        dp[0] = 1
        return dp[n]

