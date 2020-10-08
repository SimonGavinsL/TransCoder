#!/usr/bin/env python
""" generated source for module if__1__COUNT_NUMBER_OF_WAYS_TO_COVER_A_DISTANCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def printCountRec(cls, dist):
        """ generated source for method printCountRec """
        return cls.printCountRec(dist - 1) + cls.printCountRec(dist - 2) + cls.printCountRec(dist - 3)

