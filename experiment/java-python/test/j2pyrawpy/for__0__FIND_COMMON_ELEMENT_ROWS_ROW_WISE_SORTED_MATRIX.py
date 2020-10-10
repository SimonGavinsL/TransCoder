#!/usr/bin/env python
""" generated source for module for__0__FIND_COMMON_ELEMENT_ROWS_ROW_WISE_SORTED_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def findCommon(cls, mat):
        """ generated source for method findCommon """
        column = [None]*M
        min_row = int()
        i = int()
        min_row = 0
        while column[min_row] >= 0:
            while i < M:
                if mat[i][column[i]] < mat[min_row][column[min_row]]:
                    min_row = i
                i += 1
            while i < M:
                if mat[i][column[i]] > mat[min_row][column[min_row]]:
                    if column[i] == 0:
                        return -1
                    column[i] -= 1
                else:
                    eq_count += 1
                i += 1
            if eq_count == M:
                return mat[min_row][column[min_row]]
        return -1

