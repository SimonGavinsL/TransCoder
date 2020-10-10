#!/usr/bin/env python
""" generated source for module for__0__REMOVE_MINIMUM_NUMBER_ELEMENTS_NO_COMMON_ELEMENT_EXIST_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def minRemove(cls, a, b, n, m):
        """ generated source for method minRemove """
        countA = HashMap()
        countB = HashMap()
        i = 0
        while i < m:
            if countB.containsKey(b[i]):
                countB.put(b[i], countB.get(b[i]) + 1)
            else:
                countB.put(b[i], 1)
            i += 1
        res = 0
        s = countA.keySet()
        for x in s:
            if countB.containsKey(x):
                res += Math.min(countB.get(x), countA.get(x))
        return res

