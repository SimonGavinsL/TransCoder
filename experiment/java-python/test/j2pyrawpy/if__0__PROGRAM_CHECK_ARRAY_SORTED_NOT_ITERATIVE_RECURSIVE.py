#!/usr/bin/env python
""" generated source for module if__0__PROGRAM_CHECK_ARRAY_SORTED_NOT_ITERATIVE_RECURSIVE """
class X(object):
    """ generated source for class X """
    @classmethod
    def arraySortedOrNot(cls, arr, n):
        """ generated source for method arraySortedOrNot """
        if arr[n - 1] < arr[n - 2]:
            return 0
        return cls.arraySortedOrNot(arr, n - 1)

