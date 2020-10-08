#!/usr/bin/env python
""" generated source for module if__1__COUNT_NUMBER_OF_WAYS_TO_PARTITION_A_SET_INTO_K_SUBSETS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countP(cls, n, k):
        """ generated source for method countP """
        return (k * cls.countP(n - 1, k) + cls.countP(n - 1, k - 1))

