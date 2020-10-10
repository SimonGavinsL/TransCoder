#!/usr/bin/env python
""" generated source for module for__1__REMOVE_MINIMUM_NUMBER_ELEMENTS_NO_COMMON_ELEMENT_EXIST_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def minRemove(cls, a, b, n, m):
        """ generated source for method minRemove """
        countA = HashMap()
        countB = HashMap()
        res = 0
        s = countA.keySet()
        for x in s:
            if countB.containsKey(x):
                res += Math.min(countB.get(x), countA.get(x))
        return res

