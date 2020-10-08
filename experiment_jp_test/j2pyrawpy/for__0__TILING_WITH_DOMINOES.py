#!/usr/bin/env python
""" generated source for module for__0__TILING_WITH_DOMINOES """
class X(object):
    """ generated source for class X """
    @classmethod
    def countWays(cls, n):
        """ generated source for method countWays """
        A = [None]*n + 1
        B = [None]*n + 1
        A[0] = 1
        A[1] = 0
        B[0] = 0
        B[1] = 1
        return A[n]

