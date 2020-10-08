#!/usr/bin/env python
""" generated source for module for__0__PRINT_GIVEN_MATRIX_REVERSE_SPIRAL_FORM """
class X(object):
    """ generated source for class X """
    @classmethod
    def ReversespiralPrint(cls, m, n, a):
        """ generated source for method ReversespiralPrint """
        b = [None]*100
        i = int()
        k = 0
        l = 0
        z = 0
        size = m * n
        while k < m and l < n:
            while i < n:
                val = a[k][i]
                b[z] = val
                z += 1
                i += 1
            k += 1
            while i < m:
                val = a[i][n - 1]
                b[z] = val
                z += 1
                i += 1
            n -= 1
            if k < m:
                while i >= l:
                    val = a[m - 1][i]
                    b[z] = val
                    z += 1
                    i -= 1
                m -= 1
            if l < n:
                while i >= k:
                    val = a[i][l]
                    b[z] = val
                    z += 1
                    i -= 1
                l += 1

