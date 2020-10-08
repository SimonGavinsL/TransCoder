#!/usr/bin/env python
""" generated source for module for__0__FIND_ONE_EXTRA_CHARACTER_STRING_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findExtraCharcter(cls, strA, strB):
        """ generated source for method findExtraCharcter """
        res = 0
        i = int()
        while i < len(strB):
            res ^= strB.charAt(i)
            i += 1
        return (((res)))

