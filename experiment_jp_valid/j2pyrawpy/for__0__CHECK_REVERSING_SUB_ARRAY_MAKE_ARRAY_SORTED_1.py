#!/usr/bin/env python
""" generated source for module for__0__CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def checkReverse(cls, arr, n):
        """ generated source for method checkReverse """
        if n == 1:
            return True
        i = int()
        if i == n:
            return True
        j = i += 1
        while arr[j] < arr[j - 1]:
            if i > 1 and arr[j] < arr[i - 2]:
                return False
            j += 1
        if j == n:
            return True
        k = j
        if arr[k] < arr[i - 1]:
            return False
        while k > 1 and k < n:
            if arr[k] < arr[k - 1]:
                return False
            k += 1
        return True

