#!/usr/bin/env python
""" generated source for module if__2__DYNAMIC_PROGRAMMING_SET_7_COIN_CHANGE """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, S, m, n):
        """ generated source for method count """
        return cls.count(S, m - 1, n) + cls.count(S, m, n - S[m - 1])

