#!/usr/bin/env python
""" generated source for module for__0__FIND_MAXIMUM_VALUE_OF_SUM_IARRI_WITH_ONLY_ROTATIONS_ON_GIVEN_ARRAY_ALLOWED """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxSum(cls):
        """ generated source for method maxSum """
        arrSum = 0
        currVal = 0
        maxVal = currVal
        j = 1
        while j < arr.length:
            currVal = currVal + arrSum - arr.length * arr[arr.length - j]
            if currVal > maxVal:
                maxVal = currVal
            j += 1
        return maxVal

