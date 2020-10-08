#!/usr/bin/env python
""" generated source for module for__0__SMALLEST_LENGTH_STRING_WITH_REPEATED_REPLACEMENT_OF_TWO_DISTINCT_ADJACENT """
class X(object):
    """ generated source for class X """
    @classmethod
    def stringReduction(cls, str_):
        """ generated source for method stringReduction """
        n = len(str_)
        count = [None]*3
        if count[0] == n or count[1] == n or count[2] == n:
            return n
        if (count[0] % 2) == (count[1] % 2) and (count[1] % 2) == (count[2] % 2):
            return 2
        return 1

