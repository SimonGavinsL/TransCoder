#!/usr/bin/env python
""" generated source for module if__2__COUNT_EVEN_LENGTH_BINARY_SEQUENCES_WITH_SAME_SUM_OF_FIRST_AND_SECOND_HALF_BITS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countSeq(cls, n, diff):
        """ generated source for method countSeq """
        res = cls.countSeq(n - 1, diff + 1) + 2 * cls.countSeq(n - 1, diff) + cls.countSeq(n - 1, diff - 1)
        return res

