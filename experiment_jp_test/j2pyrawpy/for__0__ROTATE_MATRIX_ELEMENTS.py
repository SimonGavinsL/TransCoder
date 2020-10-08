#!/usr/bin/env python
""" generated source for module for__0__ROTATE_MATRIX_ELEMENTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def rotatematrix(cls, m, n, mat):
        """ generated source for method rotatematrix """
        row = 0
        col = 0
        prev = int()
        curr = int()
        while row < m and col < n:
            if row + 1 == m or col + 1 == n:
                break
            prev = mat[row + 1][col]
            while i < n:
                curr = mat[row][i]
                mat[row][i] = prev
                prev = curr
                i += 1
            row += 1
            while i < m:
                curr = mat[i][n - 1]
                mat[i][n - 1] = prev
                prev = curr
                i += 1
            n -= 1
            if row < m:
                while i >= col:
                    curr = mat[m - 1][i]
                    mat[m - 1][i] = prev
                    prev = curr
                    i -= 1
            m -= 1
            if col < n:
                while i >= row:
                    curr = mat[i][col]
                    mat[i][col] = prev
                    prev = curr
                    i -= 1
            col += 1

