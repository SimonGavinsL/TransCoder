#!/usr/bin/env python
""" generated source for module for__1__MAXIMUM_NUMBER_OF_TRAILING_ZEROS_IN_THE_PRODUCT_OF_THE_SUBSETS_OF_SIZE_K """
class X(object):
    """ generated source for class X """
    @classmethod
    def maximumZeros(cls, arr, n, k):
        """ generated source for method maximumZeros """
        subset = [None]*k + 1
        subset[0][0] = 0
        ans = 0
        i = 0
        while i < MAX5:
            ans = Math.max(ans, Math.min(i, subset[k][i]))
            i += 1
        return ans

