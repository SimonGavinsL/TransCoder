#!/usr/bin/env python
""" generated source for module for__0__CENTER_ELEMENT_OF_MATRIX_EQUALS_SUMS_OF_HALF_DIAGONALS """
class X(object):
    """ generated source for class X """
    @classmethod
    def HalfDiagonalSums(cls, mat, n):
        """ generated source for method HalfDiagonalSums """
        diag1_left = 0
        diag1_right = 0
        diag2_left = 0
        diag2_right = 0
        return (diag1_left == diag2_right and diag2_right == diag2_left and diag1_right == diag2_left and diag2_right == mat[n / 2][n / 2])

