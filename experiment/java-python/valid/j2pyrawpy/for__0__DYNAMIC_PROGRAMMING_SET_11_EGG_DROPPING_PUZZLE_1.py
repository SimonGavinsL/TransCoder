#!/usr/bin/env python
""" generated source for module for__0__DYNAMIC_PROGRAMMING_SET_11_EGG_DROPPING_PUZZLE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def eggDrop(cls, n, k):
        """ generated source for method eggDrop """
        eggFloor = [None]*n + 1
        res = int()
        i = int()
        j = int()
        x = int()
        while j <= k:
            j += 1
        while i <= n:
            while j <= k:
                eggFloor[i][j] = Integer.MAX_VALUE
                while x <= j:
                    res = 1 + max(eggFloor[i - 1][x - 1], eggFloor[i][j - x])
                    if res < eggFloor[i][j]:
                        eggFloor[i][j] = res
                    x += 1
                j += 1
            i += 1
        return eggFloor[n][k]

