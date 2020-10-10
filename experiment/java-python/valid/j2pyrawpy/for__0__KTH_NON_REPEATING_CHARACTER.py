#!/usr/bin/env python
""" generated source for module for__0__KTH_NON_REPEATING_CHARACTER """
class X(object):
    """ generated source for class X """
    @classmethod
    def kthNonRepeating(cls, str_, k):
        """ generated source for method kthNonRepeating """
        n = len(str_)
        count = [None]*MAX_CHAR
        index = [None]*MAX_CHAR
        i = 0
        while i < n:
            count[x] += 1
            if count[x] == 1:
                index[x] = i
            if count[x] == 2:
                index[x] = n
            i += 1
        Arrays.sort(index)
        return index[k - 1] if (index[k - 1] != n) else -1

