#!/usr/bin/env python
""" generated source for module for__0__LENGTH_LONGEST_STRICT_BITONIC_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def longLenStrictBitonicSub(cls, arr, n):
        """ generated source for method longLenStrictBitonicSub """
        inc = HashMap()
        dcr = HashMap()
        len_inc = [None]*n
        len_dcr = [None]*n
        longLen = 0
        i = n - 1
        while i >= 0:
            if dcr.containsKey(arr[i] - 1):
                len = dcr.get(arr[i] - 1)
            len_dcr[i] = len + 1
            dcr.put(arr[i], len_dcr[i])
            i -= 1
        i = 0
        while i < n:
            i += 1
        return longLen

