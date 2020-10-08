#!/usr/bin/env python
""" generated source for module if__0__DYNAMIC_PROGRAMMING_SET_7_COIN_CHANGE """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, S, m, n):
        """ generated source for method count """
        if n < 0:
            return 0
        if m <= 0 and n >= 1:
            return 0
        return cls.count(S, m - 1, n) + cls.count(S, m, n - S[m - 1])

