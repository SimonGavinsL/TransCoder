#!/usr/bin/env python
""" generated source for module for__0__SORT_ARRAY_CONVERTING_ELEMENTS_SQUARES_1 """
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
        while i >= 0 and j < n:
            if arr[i] * arr[i] < arr[j] * arr[j]:
                temp[ind] = arr[i] * arr[i]
                i -= 1
            else:
                temp[ind] = arr[j] * arr[j]
                j += 1
            ind += 1
        __ind_0 = ind
        ind += 1
        while i >= 0:
            temp[__ind_0] = arr[i] * arr[i]
            i -= 1
        __ind_1 = ind
        ind += 1
        while j < n:
            temp[__ind_1] = arr[j] * arr[j]
            j += 1
        x = 0
        while x < n:
            x += 1

