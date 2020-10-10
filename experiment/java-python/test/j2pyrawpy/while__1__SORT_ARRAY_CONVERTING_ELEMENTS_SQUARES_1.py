#!/usr/bin/env python
""" generated source for module while__1__SORT_ARRAY_CONVERTING_ELEMENTS_SQUARES_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def sortSquares(cls, arr):
        """ generated source for method sortSquares """
        n = arr.length
        k = int()
        i = k - 1
        j = k
        ind = 0
        temp = [None]*n
        __ind_0 = ind
        ind += 1
        while j < n:
            temp[__ind_0] = arr[j] * arr[j]
            j += 1

