#!/usr/bin/env python
""" generated source for module if__0__RECURSIVE_INSERTION_SORT """
class X(object):
    """ generated source for class X """
    @classmethod
    def insertionSortRecursive(cls, arr, n):
        """ generated source for method insertionSortRecursive """
        cls.insertionSortRecursive(arr, n - 1)
        last = arr[n - 1]
        j = n - 2
        while j >= 0 and arr[j] > last:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = last

