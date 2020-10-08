#!/usr/bin/env python
""" generated source for module for__0__FIND_SUM_ODD_FACTORS_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def sumofoddFactors(cls, n):
        """ generated source for method sumofoddFactors """
        res = 1
        while n % 2 == 0:
        if n >= 2:
            res *= (1 + n)
        return res

