#!/usr/bin/env python
""" generated source for module if__2__COUNT_DERANGEMENTS_PERMUTATION_SUCH_THAT_NO_ELEMENT_APPEARS_IN_ITS_ORIGINAL_POSITION """
class X(object):
    """ generated source for class X """
    @classmethod
    def countDer(cls, n):
        """ generated source for method countDer """
        return (n - 1) * (cls.countDer(n - 1) + cls.countDer(n - 2))

