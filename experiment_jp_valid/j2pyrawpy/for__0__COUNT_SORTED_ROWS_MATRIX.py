#!/usr/bin/env python
""" generated source for module for__0__COUNT_SORTED_ROWS_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def sortedCount(cls, mat, r, c):
        """ generated source for method sortedCount """
        result = 0
        i = 0
        while i < r:
            while j > 0:
                j -= 1
            if c > 1 and j == 0:
                result += 1
            i += 1
        return result

