#!/usr/bin/env python
""" generated source for module for__0__EQUILIBRIUM_INDEX_OF_AN_ARRAY_1 """
class X(object):
    """ generated source for class X """
    def equilibrium(self, arr, n):
        """ generated source for method equilibrium """
        sum = 0
        leftsum = 0
        i = 0
        while i < n:
            sum -= arr[i]
            if leftsum == sum:
                return i
            leftsum += arr[i]
            i += 1
        return -1

