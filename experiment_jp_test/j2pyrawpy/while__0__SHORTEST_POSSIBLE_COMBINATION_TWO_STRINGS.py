#!/usr/bin/env python
""" generated source for module while__0__SHORTEST_POSSIBLE_COMBINATION_TWO_STRINGS """
class X(object):
    """ generated source for class X """
    @classmethod
    def printSuperSeq(cls, a, b):
        """ generated source for method printSuperSeq """
        m = len(a)
        n = len(b)
        dp = [None]*m + 1
        res = " "
        i = m
        j = n
        while i > 0:
            res = a.charAt(i - 1) + res
            i -= 1
        while j > 0:
            res = b.charAt(j - 1) + res
            j -= 1
        print res

