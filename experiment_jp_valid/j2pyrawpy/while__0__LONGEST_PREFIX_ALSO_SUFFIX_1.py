#!/usr/bin/env python
""" generated source for module while__0__LONGEST_PREFIX_ALSO_SUFFIX_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def longestPrefixSuffix(cls, s):
        """ generated source for method longestPrefixSuffix """
        n = len(s)
        lps = [None]*n
        lps[0] = 0
        len = 0
        i = 1
        res = lps[n - 1]
        return n / 2 if (res > n / 2) else res

