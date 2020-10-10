#!/usr/bin/env python
""" generated source for module while__0__RECURSIVE_INSERTION_SORT """
class X(object):
    """ generated source for class X """
    @classmethod
    def insertionSortRecursive(cls, arr, n):
        """ generated source for method insertionSortRecursive """
        cls.insertionSortRecursive(arr, n - 1)
        last = arr[n - 1]
        j = n - 2
        arr[j + 1] = last

