#!/usr/bin/env python
""" generated source for module if__1__SHORTEST_COMMON_SUPERSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def superSeq(cls, X, Y, m, n):
        """ generated source for method superSeq """
        if X.charAt(m - 1) == Y.charAt(n - 1):
            return 1 + cls.superSeq(X, Y, m - 1, n - 1)
        return 1 + Math.min(cls.superSeq(X, Y, m - 1, n), cls.superSeq(X, Y, m, n - 1))

