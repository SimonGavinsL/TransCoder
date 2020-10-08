#!/usr/bin/env python
""" generated source for module if__0__GIVEN_TWO_STRINGS_FIND_FIRST_STRING_SUBSEQUENCE_SECOND """
class X(object):
    """ generated source for class X """
    @classmethod
    def isSubSequence(cls, str1, str2, m, n):
        """ generated source for method isSubSequence """
        if n == 0:
            return False
        if str1.charAt(m - 1) == str2.charAt(n - 1):
            return cls.isSubSequence(str1, str2, m - 1, n - 1)
        return cls.isSubSequence(str1, str2, m, n - 1)

