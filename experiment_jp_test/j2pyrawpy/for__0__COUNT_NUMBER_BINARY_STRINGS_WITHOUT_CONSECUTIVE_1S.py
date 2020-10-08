#!/usr/bin/env python
""" generated source for module for__0__COUNT_NUMBER_BINARY_STRINGS_WITHOUT_CONSECUTIVE_1S """
class X(object):
    """ generated source for class X """
    @classmethod
    def countStrings(cls, n):
        """ generated source for method countStrings """
        a = [None]*n
        b = [None]*n
        a[0] = b[0] = 1
        return a[n - 1] + b[n - 1]

