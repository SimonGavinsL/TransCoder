#!/usr/bin/env python
""" generated source for module for__0__CONVERTING_ONE_STRING_USING_APPEND_DELETE_LAST_OPERATIONS """
class X(object):
    """ generated source for class X """
    @classmethod
    def isConvertible(cls, str1, str2, k):
        """ generated source for method isConvertible """
        if len((str1) + len(str2)) < k:
            return True
        commonLength = 0
        if (k - len(str1) - len(str2) + 2 * commonLength) % 2 == 0:
            return True
        return False

