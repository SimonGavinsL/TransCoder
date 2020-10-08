#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_NUMBER_OF_TRAILING_ZEROS_IN_THE_PRODUCT_OF_THE_SUBSETS_OF_SIZE_K """
class X(object):
    """ generated source for class X """
    @classmethod
    def maximumZeros(cls, arr, n, k):
        """ generated source for method maximumZeros """
        subset = [None]*k + 1
        subset[0][0] = 0
        p = 0
        while p < n:
            while arr[p] % 2 == 0:
                pw2 += 1
                arr[p] /= 2
            while arr[p] % 5 == 0:
                pw5 += 1
                arr[p] /= 5
            while i >= 0:
                while j < MAX5:
                    if subset[i][j] != -1:
                        subset[i + 1][j + pw5] = Math.max(subset[i + 1][j + pw5], subset[i][j] + pw2)
                    j += 1
                i -= 1
            p += 1
        ans = 0
        i = 0
        while i < MAX5:
            ans = Math.max(ans, Math.min(i, subset[k][i]))
            i += 1
        return ans

