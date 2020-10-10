#!/usr/bin/env python
""" generated source for module for__0__CHANGE_ARRAY_PERMUTATION_NUMBERS_1_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def makePermutation(cls, a, n):
        """ generated source for method makePermutation """
        count = HashMap()
        next_missing = 1
        i = 0
        while i < n:
            if count.containsKey(a[i]) and count.get(a[i]) != 1 or a[i] > n or a[i] < 1:
                count.put(a[i], count.get(a[i]) - 1)
                while count.containsKey(next_missing):
                a[i] = next_missing
                count.put(next_missing, 1)
            i += 1

