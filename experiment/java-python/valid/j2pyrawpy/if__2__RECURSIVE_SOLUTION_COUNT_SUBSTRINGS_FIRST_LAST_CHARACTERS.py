#!/usr/bin/env python
""" generated source for module if__2__RECURSIVE_SOLUTION_COUNT_SUBSTRINGS_FIRST_LAST_CHARACTERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countSubstrs(cls, str_, i, j, n):
        """ generated source for method countSubstrs """
        res = cls.countSubstrs(str_, i + 1, j, n - 1) + cls.countSubstrs(str_, i, j - 1, n - 1) - cls.countSubstrs(str_, i + 1, j - 1, n - 2)
        return res

