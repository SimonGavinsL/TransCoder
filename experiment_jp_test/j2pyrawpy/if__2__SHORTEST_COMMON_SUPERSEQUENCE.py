#!/usr/bin/env python
""" generated source for module if__2__SHORTEST_COMMON_SUPERSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def superSeq(cls, X, Y, m, n):
        """ generated source for method superSeq """
        return 1 + Math.min(cls.superSeq(X, Y, m - 1, n), cls.superSeq(X, Y, m, n - 1))

