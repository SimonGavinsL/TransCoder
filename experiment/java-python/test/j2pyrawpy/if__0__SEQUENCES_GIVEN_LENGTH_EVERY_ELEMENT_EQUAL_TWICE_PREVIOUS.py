#!/usr/bin/env python
""" generated source for module if__0__SEQUENCES_GIVEN_LENGTH_EVERY_ELEMENT_EQUAL_TWICE_PREVIOUS """
class X(object):
    """ generated source for class X """
    @classmethod
    def getTotalNumberOfSequences(cls, m, n):
        """ generated source for method getTotalNumberOfSequences """
        if n == 0:
            return 1
        return cls.getTotalNumberOfSequences(m - 1, n) + cls.getTotalNumberOfSequences(m / 2, n - 1)

