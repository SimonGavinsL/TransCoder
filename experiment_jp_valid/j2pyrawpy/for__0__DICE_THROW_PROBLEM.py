#!/usr/bin/env python
""" generated source for module for__0__DICE_THROW_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def findWays(cls, m, n, x):
        """ generated source for method findWays """
        table = [None]*n + 1
        i = 2
        while i <= n:
            while j <= x:
                while k < j and k <= m:
                    k += 1
                j += 1
            i += 1
        return table[n][x]

