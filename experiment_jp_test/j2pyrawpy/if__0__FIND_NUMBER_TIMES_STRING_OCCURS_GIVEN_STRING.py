#!/usr/bin/env python
""" generated source for module if__0__FIND_NUMBER_TIMES_STRING_OCCURS_GIVEN_STRING """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, a, b, m, n):
        """ generated source for method count """
        if m == 0:
            return 0
        if a.charAt(m - 1) == b.charAt(n - 1):
            return cls.count(a, b, m - 1, n - 1) + cls.count(a, b, m - 1, n)
        else:
            return cls.count(a, b, m - 1, n)

