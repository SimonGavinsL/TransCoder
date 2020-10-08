#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_NUMBER_CHARACTERS_TWO_CHARACTER_STRING_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def maximumChars(cls, str_):
        """ generated source for method maximumChars """
        n = len(str_)
        res = -1
        firstInd = [None]*MAX_CHAR
        i = 0
        while i < n:
            if first_ind == -1:
                firstInd[str_.charAt(i)] = i
            else:
                res = Math.max(res, Math.abs(i - first_ind - 1))
            i += 1
        return res

