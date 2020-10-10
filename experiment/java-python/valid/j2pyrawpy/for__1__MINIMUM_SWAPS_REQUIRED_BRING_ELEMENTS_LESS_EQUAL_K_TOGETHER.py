#!/usr/bin/env python
""" generated source for module for__1__MINIMUM_SWAPS_REQUIRED_BRING_ELEMENTS_LESS_EQUAL_K_TOGETHER """
class X(object):
    """ generated source for class X """
    @classmethod
    def minSwap(cls, arr, n, k):
        """ generated source for method minSwap """
        count = 0
        bad = 0
        ans = bad
        i = 0
        j = count
        while j < n:
            if arr[i] > k:
                bad -= 1
            if arr[j] > k:
                bad += 1
            ans = Math.min(ans, bad)
            j += 1
        return ans

