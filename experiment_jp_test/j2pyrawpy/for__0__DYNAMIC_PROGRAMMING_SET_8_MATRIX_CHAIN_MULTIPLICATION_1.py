#!/usr/bin/env python
""" generated source for module for__0__DYNAMIC_PROGRAMMING_SET_8_MATRIX_CHAIN_MULTIPLICATION_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def MatrixChainOrder(cls, p, n):
        """ generated source for method MatrixChainOrder """
        m = [None]*n
        i = int()
        j = int()
        k = int()
        L = int()
        q = int()
        while L < n:
            while i < n - L + 1:
                j = i + L - 1
                if j == n:
                    continue 
                m[i][j] = Integer.MAX_VALUE
                while k <= j - 1:
                    q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if q < m[i][j]:
                        m[i][j] = q
                    k += 1
                i += 1
            L += 1
        return m[1][n - 1]

