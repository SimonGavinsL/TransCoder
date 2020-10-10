#!/usr/bin/env python
""" generated source for module for__2__PARTITION_NUMBER_TWO_DIVISBLE_PARTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def findDivision(cls, str_, a, b):
        """ generated source for method findDivision """
        len = len(str_)
        lr = [None]*len + 1
        lr[0] = ((str_.charAt(0)) - ('0')) % a
        rl = [None]*len + 1
        rl[len - 1] = ((str_.charAt(len - 1)) - ('0')) % b
        power10 = 10
        print " NO "

