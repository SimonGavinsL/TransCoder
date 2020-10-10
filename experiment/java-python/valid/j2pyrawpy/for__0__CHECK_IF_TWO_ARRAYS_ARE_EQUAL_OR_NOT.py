#!/usr/bin/env python
""" generated source for module for__0__CHECK_IF_TWO_ARRAYS_ARE_EQUAL_OR_NOT """
class X(object):
    """ generated source for class X """
    @classmethod
    def areEqual(cls, arr1, arr2):
        """ generated source for method areEqual """
        n = arr1.length
        m = arr2.length
        if n != m:
            return False
        Arrays.sort(arr1)
        Arrays.sort(arr2)
        return True

