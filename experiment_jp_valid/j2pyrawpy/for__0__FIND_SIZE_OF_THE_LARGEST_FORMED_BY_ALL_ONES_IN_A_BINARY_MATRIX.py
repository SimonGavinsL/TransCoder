#!/usr/bin/env python
""" generated source for module for__0__FIND_SIZE_OF_THE_LARGEST_FORMED_BY_ALL_ONES_IN_A_BINARY_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def findLargestPlus(cls, mat):
        """ generated source for method findLargestPlus """
        left = [None]*N
        right = [None]*N
        top = [None]*N
        bottom = [None]*N
        i = 0
        while i < N:
            while j < N:
                if mat[i][j] == 1:
                    left[i][j] = left[i][j - 1] + 1
                else:
                    left[i][j] = 0
                if mat[j][i] == 1:
                    top[j][i] = top[j - 1][i] + 1
                else:
                    top[j][i] = 0
                j = N - 1 - j
                if mat[j][i] == 1:
                    bottom[j][i] = bottom[j + 1][i] + 1
                else:
                    bottom[j][i] = 0
                if mat[i][j] == 1:
                    right[i][j] = right[i][j + 1] + 1
                else:
                    right[i][j] = 0
                j = N - 1 - j
                j += 1
            i += 1
        n = 0
        i = 0
        while i < N:
            while j < N:
                if len > n:
                    n = len
                j += 1
            i += 1
        if n > 0:
            return 4 * (n - 1) + 1
        return 0

