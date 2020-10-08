#!/usr/bin/env python
""" generated source for module for__0__COUNT_WAYS_DIVIDE_CIRCLE_USING_N_NON_INTERSECTING_CHORDS """
class X(object):
    """ generated source for class X """
    @classmethod
    def chordCnt(cls, A):
        """ generated source for method chordCnt """
        n = 2 * A
        dpArray = [None]*n + 1
        dpArray[0] = 1
        dpArray[2] = 1
        return dpArray[n]

