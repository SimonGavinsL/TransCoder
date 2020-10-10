#!/usr/bin/env python
""" generated source for module for__0__LONGEST_COMMON_INCREASING_SUBSEQUENCE_LCS_LIS """
class X(object):
    """ generated source for class X """
    @classmethod
    def LCIS(cls, arr1, n, arr2, m):
        """ generated source for method LCIS """
        table = [None]*m
        i = 0
        while i < n:
            while j < m:
                if arr1[i] == arr2[j]:
                    if current + 1 > table[j]:
                        table[j] = current + 1
                if arr1[i] > arr2[j]:
                    if table[j] > current:
                        current = table[j]
                j += 1
            i += 1
        result = 0
        i = 0
        while i < m:
            i += 1
        return result

