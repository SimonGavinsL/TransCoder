#!/usr/bin/env python
""" generated source for module for__1__KTH_NON_REPEATING_CHARACTER """
class X(object):
    """ generated source for class X """
    @classmethod
    def kthNonRepeating(cls, str_, k):
        """ generated source for method kthNonRepeating """
        n = len(str_)
        count = [None]*MAX_CHAR
        index = [None]*MAX_CHAR
        Arrays.sort(index)
        return index[k - 1] if (index[k - 1] != n) else -1

