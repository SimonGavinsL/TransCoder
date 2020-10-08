#!/usr/bin/env python
""" generated source for module for__0__MINIMUM_OPERATION_MAKE_ELEMENTS_EQUAL_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def minOperation(cls, arr, n):
        """ generated source for method minOperation """
        hash = HashMap()
        max_count = 0
        s = hash.keySet()
        for i in s:
            if max_count < hash.get(i):
                max_count = hash.get(i)
        return (n - max_count)

