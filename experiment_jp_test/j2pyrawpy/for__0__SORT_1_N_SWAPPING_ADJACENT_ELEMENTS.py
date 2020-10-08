#!/usr/bin/env python
""" generated source for module for__0__SORT_1_N_SWAPPING_ADJACENT_ELEMENTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def sortedAfterSwap(cls, A, B, n):
        """ generated source for method sortedAfterSwap """
        i = int()
        j = int()
        while i < n:
            if A[i] != i + 1:
                return False
            i += 1
        return True

