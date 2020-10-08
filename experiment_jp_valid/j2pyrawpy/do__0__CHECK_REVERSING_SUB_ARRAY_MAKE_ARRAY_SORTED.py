#!/usr/bin/env python
""" generated source for module do__0__CHECK_REVERSING_SUB_ARRAY_MAKE_ARRAY_SORTED """
class X(object):
    """ generated source for class X """
    @classmethod
    def checkReverse(cls, arr, n):
        """ generated source for method checkReverse """
        temp = [None]*n
        i = 0
        while i < n:
            temp[i] = arr[i]
            i += 1
        Arrays.sort(temp)
        front = int()
        while front < n:
            if temp[front] != arr[front]:
                break
            front += 1
        back = int()
        while back >= 0:
            if temp[back] != arr[back]:
                break
            back -= 1
        if front >= back:
            return True
        return True

