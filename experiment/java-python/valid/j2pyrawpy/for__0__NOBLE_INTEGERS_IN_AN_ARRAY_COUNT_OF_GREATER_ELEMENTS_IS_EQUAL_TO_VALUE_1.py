#!/usr/bin/env python
""" generated source for module for__0__NOBLE_INTEGERS_IN_AN_ARRAY_COUNT_OF_GREATER_ELEMENTS_IS_EQUAL_TO_VALUE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def nobleInteger(cls, arr):
        """ generated source for method nobleInteger """
        Arrays.sort(arr)
        n = arr.length
        if arr[n - 1] == 0:
            return arr[n - 1]
        return -1

