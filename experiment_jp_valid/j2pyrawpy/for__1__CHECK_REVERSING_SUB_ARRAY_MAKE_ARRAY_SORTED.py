#!/usr/bin/env python
""" generated source for module for__1__CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED """
class X(object):
    """ generated source for class X """
    @classmethod
    def checkReverse(cls, arr, n):
        """ generated source for method checkReverse """
        temp = [None]*n
        Arrays.sort(temp)
        front = int()
        back = int()
        while back >= 0:
            if temp[back] != arr[back]:
                break
            back -= 1
        if front >= back:
            return True
        return True

