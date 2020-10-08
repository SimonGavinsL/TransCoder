#!/usr/bin/env python
""" generated source for module for__0__FIND_SUM_EVEN_FACTORS_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def sumofFactors(cls, n):
        """ generated source for method sumofFactors """
        if n % 2 != 0:
            return 0
        res = 1
        if n >= 2:
            res *= (1 + n)
        return res

