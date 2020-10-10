#!/usr/bin/env python
""" generated source for module if__0__LONGEST_GEOMETRIC_PROGRESSION """
class X(object):
    """ generated source for class X """
    @classmethod
    def lenOfLongestGP(cls, set, n):
        """ generated source for method lenOfLongestGP """
        if n == 2:
            return (1 if set[1] % set[0] == 0 else 0)
        Arrays.sort(set)
        L = [None]*n
        llgp = 1
        return llgp

