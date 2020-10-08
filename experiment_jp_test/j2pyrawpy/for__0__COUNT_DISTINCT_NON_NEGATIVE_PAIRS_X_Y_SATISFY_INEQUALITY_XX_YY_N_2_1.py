#!/usr/bin/env python
""" generated source for module for__0__COUNT_DISTINCT_NON_NEGATIVE_PAIRS_X_Y_SATISFY_INEQUALITY_XX_YY_N_2_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countSolutions(cls, n):
        """ generated source for method countSolutions """
        x = 0
        yCount = int()
        res = 0
        while yCount != 0:
            res += yCount
            x += 1
            while yCount != 0 and (x * x + (yCount - 1) * (yCount - 1) >= n):
        return res

