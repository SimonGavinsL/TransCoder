#!/usr/bin/env python
""" generated source for module while__0__WORD_WRAP_PROBLEM_SPACE_OPTIMIZED_SOLUTION """
class X(object):
    """ generated source for class X """
    @classmethod
    def solveWordWrap(cls, arr, n, k):
        """ generated source for method solveWordWrap """
        i = int()
        j = int()
        currlen = int()
        cost = int()
        dp = [None]*n
        ans = [None]*n
        dp[n - 1] = 0
        ans[n - 1] = n - 1
        i = 0

