#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_SUM_INCREASING_ORDER_ELEMENTS_N_ARRAYS """
class X(object):
    """ generated source for class X """
    @classmethod
    def maximumSum(cls, a, n):
        """ generated source for method maximumSum """
        sum = a[n - 1][M - 1]
        prev = a[n - 1][M - 1]
        i = int()
        j = int()
        while i >= 0:
            while j >= 0:
                if a[i][j] < prev:
                    prev = a[i][j]
                    sum += prev
                    break
                j -= 1
            if j == -1:
                return 0
            i -= 1
        return sum

