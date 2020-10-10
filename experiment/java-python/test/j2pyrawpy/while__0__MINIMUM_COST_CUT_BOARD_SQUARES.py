#!/usr/bin/env python
""" generated source for module while__0__MINIMUM_COST_CUT_BOARD_SQUARES """
class X(object):
    """ generated source for class X """
    @classmethod
    def minimumCostOfBreaking(cls, X, Y, m, n):
        """ generated source for method minimumCostOfBreaking """
        res = 0
        Arrays.sort(X, Collections.reverseOrder())
        Arrays.sort(Y, Collections.reverseOrder())
        hzntl = 1
        vert = 1
        i = 0
        j = 0
        total = 0
        while i < m:
        res += total * vert
        total = 0
        while j < n:
        res += total * hzntl
        return res

