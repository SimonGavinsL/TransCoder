#!/usr/bin/env python
""" generated source for module for__0__FREQUENT_ELEMENT_ARRAY_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def mostFrequent(cls, arr, n):
        """ generated source for method mostFrequent """
        hp = HashMap()
        max_count = 0
        res = -1
        for val in hp.entrySet():
            if max_count < val.getValue():
                res = val.getKey()
                max_count = val.getValue()
        return res

