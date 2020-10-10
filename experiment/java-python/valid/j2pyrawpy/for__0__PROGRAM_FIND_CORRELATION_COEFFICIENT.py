#!/usr/bin/env python
""" generated source for module for__0__PROGRAM_FIND_CORRELATION_COEFFICIENT """
class X(object):
    """ generated source for class X """
    @classmethod
    def correlationCoefficient(cls, X, Y, n):
        """ generated source for method correlationCoefficient """
        sum_X = 0
        sum_Y = 0
        sum_XY = 0
        squareSum_X = 0
        squareSum_Y = 0
        corr = ((n * sum_XY - sum_X * sum_Y)) / ((Math.sqrt((n * squareSum_X - sum_X * sum_X) * (n * squareSum_Y - sum_Y * sum_Y))))
        return corr

