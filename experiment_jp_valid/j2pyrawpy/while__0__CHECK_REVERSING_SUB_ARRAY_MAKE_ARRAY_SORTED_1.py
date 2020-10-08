#!/usr/bin/env python
""" generated source for module while__0__CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def checkReverse(cls, arr, n):
        """ generated source for method checkReverse """
        i = int()
        j = i += 1
        k = j
        while k > 1 and k < n:
            if arr[k] < arr[k - 1]:
                return False
            k += 1
        return True

