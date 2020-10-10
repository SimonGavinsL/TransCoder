#!/usr/bin/env python
""" generated source for module for__0__DICE_THROW_PROBLEM_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findWays(cls, f, d, s):
        """ generated source for method findWays """
        mem = [None]*d + 1
        mem[0][0] = 1
        return mem[d][s]

