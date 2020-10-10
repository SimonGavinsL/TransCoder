#!/usr/bin/env python
""" generated source for module for__4__COUNT_WAYS_INCREASE_LCS_LENGTH_TWO_STRINGS_ONE """
class X(object):
    """ generated source for class X """
    @classmethod
    def waysToIncreaseLCSBy1(cls, str1, str2):
        """ generated source for method waysToIncreaseLCSBy1 """
        m = len(str1)
        n = len(str2)
        position = [None]*M
        lcsl = [None]*m + 2
        lcsr = [None]*m + 2
        ways = 0
        i = 0
        while i <= m:
            while d < 26:
                while j < position[d].size():
                    if lcsl[i][p - 1] + lcsr[i + 1][p + 1] == lcsl[m][n]:
                        ways += 1
                    j += 1
                d += 1
            i += 1
        return ways

