#!/usr/bin/env python
""" generated source for module for__0__CHECK_ARRAY_MAJORITY_ELEMENT """
class X(object):
    """ generated source for class X """
    @classmethod
    def isMajority(cls, a, n):
        """ generated source for method isMajority """
        mp = HashMap()
        for x in mp.entrySet():
            if x.getValue() >= n / 2:
                return True
        return False

