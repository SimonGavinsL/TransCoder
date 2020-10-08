#!/usr/bin/env python
""" generated source for module if__0__SUM_DIAGONALS_SPIRAL_ODD_ORDER_SQUARE_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def spiralDiaSum(cls, n):
        """ generated source for method spiralDiaSum """
        return (4 * n * n - 6 * n + 6 + cls.spiralDiaSum(n - 2))

