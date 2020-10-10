#!/usr/bin/env python
""" generated source for module for__0__SORT_1_N_SWAPPING_ADJACENT_ELEMENTS_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def sortedAfterSwap(cls, A, B, n):
        """ generated source for method sortedAfterSwap """
        t = 0
        i = 0
        while i < n:
            if A[i] != i + 1:
                return 0
            i += 1
        return 1

