#!/usr/bin/env python
""" generated source for module for__0__FIND_MINIMUM_NUMBER_OF_COINS_THAT_MAKE_A_CHANGE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def minCoins(cls, coins, m, V):
        """ generated source for method minCoins """
        table = [None]*V + 1
        table[0] = 0
        i = 1
        while i <= V:
            while j < m:
                j += 1
            i += 1
        return table[V]

