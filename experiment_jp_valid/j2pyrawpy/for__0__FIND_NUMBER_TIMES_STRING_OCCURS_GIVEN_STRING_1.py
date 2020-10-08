#!/usr/bin/env python
""" generated source for module for__0__FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, a, b):
        """ generated source for method count """
        m = len(a)
        n = len(b)
        lookup = [None]*m + 1
        i = 0
        while i <= m:
            i += 1
        i = 1
        while i <= m:
            while j <= n:
                if a.charAt(i - 1) == b.charAt(j - 1):
                    lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
                else:
                    lookup[i][j] = lookup[i - 1][j]
                j += 1
            i += 1
        return lookup[m][n]

