#!/usr/bin/env python
""" generated source for module for__1__FIND_A_SPECIFIC_PAIR_IN_MATRIX_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findMaxValue(cls, N, mat):
        """ generated source for method findMaxValue """
        maxValue = Integer.MIN_VALUE
        maxArr = [None]*N
        maxArr[N - 1][N - 1] = mat[N - 1][N - 1]
        maxv = mat[N - 1][N - 1]
        maxv = mat[N - 1][N - 1]
        i = N - 2
        while i >= 0:
            while j >= 0:
                if maxArr[i + 1][j + 1] - mat[i][j] > maxValue:
                    maxValue = maxArr[i + 1][j + 1] - mat[i][j]
                maxArr[i][j] = Math.max(mat[i][j], Math.max(maxArr[i][j + 1], maxArr[i + 1][j]))
                j -= 1
            i -= 1
        return maxValue

