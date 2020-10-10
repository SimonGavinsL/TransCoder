#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_DIFFERENCE_SUM_ELEMENTS_TWO_ROWS_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxRowDiff(cls, mat, m, n):
        """ generated source for method maxRowDiff """
        rowSum = [None]*m
        max_diff = rowSum[1] - rowSum[0]
        min_element = rowSum[0]
        i = 1
        while i < m:
            if rowSum[i] - min_element > max_diff:
                max_diff = rowSum[i] - min_element
            if rowSum[i] < min_element:
                min_element = rowSum[i]
            i += 1
        return max_diff

