#!/usr/bin/env python
""" generated source for module for__0__CHECK_ROWS_MATRIX_CIRCULAR_ROTATIONS """
class X(object):
    """ generated source for class X """
    @classmethod
    def isPermutedMatrix(cls, mat, n):
        """ generated source for method isPermutedMatrix """
        str_cat = " "
        str_cat = str_cat + str_cat
        i = 1
        while i < n:
            while j < n:
                curr_str = curr_str + " - " + String.valueOf(mat[i][j])
                j += 1
            if str_cat.contentEquals(curr_str):
                return False
            i += 1
        return True

