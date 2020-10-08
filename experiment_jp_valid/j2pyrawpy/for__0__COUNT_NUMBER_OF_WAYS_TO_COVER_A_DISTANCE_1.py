#!/usr/bin/env python
""" generated source for module for__0__COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def printCountDP(cls, dist):
        """ generated source for method printCountDP """
        count = [None]*dist + 1
        count[0] = 1
        count[1] = 1
        count[2] = 2
        return count[dist]

