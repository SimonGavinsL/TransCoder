#!/usr/bin/env python
""" generated source for module for__1__MINIMUM_STEPS_TO_DELETE_A_STRING_AFTER_REPEATED_DELETION_OF_PALINDROME_SUBSTRINGS """
class X(object):
    """ generated source for class X """
    @classmethod
    def minStepToDeleteString(cls, str_):
        """ generated source for method minStepToDeleteString """
        N = len(str_)
        dp = [None]*N + 1
        return dp[0][N - 1]

