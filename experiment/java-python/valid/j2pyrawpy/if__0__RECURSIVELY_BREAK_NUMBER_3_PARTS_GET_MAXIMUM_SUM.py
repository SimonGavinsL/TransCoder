#!/usr/bin/env python
""" generated source for module if__0__RECURSIVELY_BREAK_NUMBER_3_PARTS_GET_MAXIMUM_SUM """
class X(object):
    """ generated source for class X """
    @classmethod
    def breakSum(cls, n):
        """ generated source for method breakSum """
        return Math.max((cls.breakSum(n / 2) + cls.breakSum(n / 3) + cls.breakSum(n / 4)), n)

