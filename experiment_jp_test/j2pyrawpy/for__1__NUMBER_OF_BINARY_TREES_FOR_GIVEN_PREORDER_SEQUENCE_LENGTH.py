#!/usr/bin/env python
""" generated source for module for__1__NUMBER_OF_BINARY_TREES_FOR_GIVEN_PREORDER_SEQUENCE_LENGTH """
class X(object):
    """ generated source for class X """
    @classmethod
    def countTrees(cls, n):
        """ generated source for method countTrees """
        BT = [None]*n + 1
        BT[0] = BT[1] = 1
        return BT[n]

