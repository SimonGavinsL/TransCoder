#!/usr/bin/env python
""" generated source for module for__0__COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countDer(cls, n):
        """ generated source for method countDer """
        der = [None]*n + 1
        der[0] = 1
        der[1] = 0
        der[2] = 1
        return der[n]

