#!/usr/bin/env python
""" generated source for module if__0__HOW_TO_CHECK_IF_A_GIVEN_ARRAY_REPRESENTS_A_BINARY_HEAP """
class X(object):
    """ generated source for class X """
    @classmethod
    def isHeap(cls, arr, i, n):
        """ generated source for method isHeap """
        if arr[i] >= arr[2 * i + 1] and arr[i] >= arr[2 * i + 2] and cls.isHeap(arr, 2 * i + 1, n) and cls.isHeap(arr, 2 * i + 2, n):
            return True
        return False

