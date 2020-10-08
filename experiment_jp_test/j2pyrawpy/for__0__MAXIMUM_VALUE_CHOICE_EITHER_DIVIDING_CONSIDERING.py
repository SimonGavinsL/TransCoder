#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_VALUE_CHOICE_EITHER_DIVIDING_CONSIDERING """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxDP(cls, n):
        """ generated source for method maxDP """
        res = [None]*n + 1
        res[0] = 0
        res[1] = 1
        return res[n]

