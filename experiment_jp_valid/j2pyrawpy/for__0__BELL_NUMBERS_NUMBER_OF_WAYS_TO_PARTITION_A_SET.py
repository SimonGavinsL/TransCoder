#!/usr/bin/env python
""" generated source for module for__0__BELL_NUMBERS_NUMBER_OF_WAYS_TO_PARTITION_A_SET """
class X(object):
    """ generated source for class X """
    @classmethod
    def bellNumber(cls, n):
        """ generated source for method bellNumber """
        bell = [None]*n + 1
        bell[0][0] = 1
        return bell[n][0]

