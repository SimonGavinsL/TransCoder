#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_TIME_WRITE_CHARACTERS_USING_INSERT_DELETE_COPY_OPERATION """
class X(object):
    """ generated source for class X """
    @classmethod
    def minTimeForWritingChars(cls, N, insert, remove, copy):
        """ generated source for method minTimeForWritingChars """
        if N == 0:
            return 0
        if N == 1:
            return insert
        dp = [None]*N + 1
        return dp[N]

