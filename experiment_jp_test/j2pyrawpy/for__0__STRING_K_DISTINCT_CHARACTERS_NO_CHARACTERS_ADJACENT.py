#!/usr/bin/env python
""" generated source for module for__0__STRING_K_DISTINCT_CHARACTERS_NO_CHARACTERS_ADJACENT """
class X(object):
    """ generated source for class X """
    @classmethod
    def findString(cls, n, k):
        """ generated source for method findString """
        res = " "
        count = 0
        i = 0
        while i < n - k:
            res = res + ((count))
            count += 1
            if count == k:
                count = 0
            i += 1
        return res

