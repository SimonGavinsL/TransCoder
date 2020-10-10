#!/usr/bin/env python
""" generated source for module if__0__HOW_TO_TURN_OFF_A_PARTICULAR_BIT_IN_A_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def turnOffK(cls, n, k):
        """ generated source for method turnOffK """
        return (n & ~(1 << (k - 1)))

