#!/usr/bin/env python
""" generated source for module if__0__LOWER_INSERTION_POINT """
class X(object):
    """ generated source for class X """
    @classmethod
    def LowerInsertionPoint(cls, arr, n, X):
        """ generated source for method LowerInsertionPoint """
        lowerPnt = 0
        i = 1
        while i < n and arr[i] < X:
            lowerPnt = i
            i = i * 2
        while lowerPnt < n and arr[lowerPnt] < X:
        return lowerPnt

