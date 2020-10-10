#!/usr/bin/env python
""" generated source for module for__0__WAYS_TO_WRITE_N_AS_SUM_OF_TWO_OR_MORE_POSITIVE_INTEGERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countWays(cls, n):
        """ generated source for method countWays """
        table = [None]*n + 1
        Arrays.fill(table, 0)
        table[0] = 1
        return table[n]

