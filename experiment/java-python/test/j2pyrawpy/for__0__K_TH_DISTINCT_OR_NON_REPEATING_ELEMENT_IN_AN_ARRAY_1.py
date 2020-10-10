#!/usr/bin/env python
""" generated source for module for__0__K_TH_DISTINCT_OR_NON_REPEATING_ELEMENT_IN_AN_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def printKDistinct(cls, arr, n, k):
        """ generated source for method printKDistinct """
        h = HashMap()
        if len(h) < k:
            return -1
        dist_count = 0
        i = 0
        while i < n:
            if h.get(arr[i]) == 1:
                dist_count += 1
            if dist_count == k:
                return arr[i]
            i += 1
        return -1

