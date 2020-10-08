#!/usr/bin/env python
""" generated source for module for__0__GOLD_MINE_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def getMaxGold(cls, gold, m, n):
        """ generated source for method getMaxGold """
        goldTable = [None]*m
        col = n - 1
        while col >= 0:
            while row < m:
                goldTable[row][col] = gold[row][col] + Math.max(right, Math.max(right_up, right_down))
                row += 1
            col -= 1
        res = goldTable[0][0]
        i = 1
        while i < m:
            i += 1
        return res

