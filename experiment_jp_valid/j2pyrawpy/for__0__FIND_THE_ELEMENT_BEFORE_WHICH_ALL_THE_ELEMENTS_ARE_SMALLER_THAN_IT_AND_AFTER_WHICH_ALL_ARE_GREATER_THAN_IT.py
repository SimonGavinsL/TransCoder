#!/usr/bin/env python
""" generated source for module for__0__FIND_THE_ELEMENT_BEFORE_WHICH_ALL_THE_ELEMENTS_ARE_SMALLER_THAN_IT_AND_AFTER_WHICH_ALL_ARE_GREATER_THAN_IT """
class X(object):
    """ generated source for class X """
    @classmethod
    def findElement(cls, arr, n):
        """ generated source for method findElement """
        leftMax = [None]*n
        leftMax[0] = Integer.MIN_VALUE
        rightMin = Integer.MAX_VALUE
        i = n - 1
        while i >= 0:
            if leftMax[i] < arr[i] and rightMin > arr[i]:
                return i
            rightMin = Math.min(rightMin, arr[i])
            i -= 1
        return -1

