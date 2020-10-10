#!/usr/bin/env python
""" generated source for module for__1__COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def numberOfPaths(cls, m, n):
        """ generated source for method numberOfPaths """
        count = [None]*m
        i = 1
        while i < m:
            while j < n:
                j += 1
            i += 1
        return count[m - 1][n - 1]

