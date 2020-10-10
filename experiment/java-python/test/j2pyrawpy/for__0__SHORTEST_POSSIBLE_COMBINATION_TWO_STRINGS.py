#!/usr/bin/env python
""" generated source for module for__0__SHORTEST_POSSIBLE_COMBINATION_TWO_STRINGS """
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
        while i > 0 and j > 0:
            if a.charAt(i - 1) == b.charAt(j - 1):
                res = a.charAt(i - 1) + res
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
                res = a.charAt(i - 1) + res
                i -= 1
            else:
                res = b.charAt(j - 1) + res
                j -= 1
        while i > 0:
            res = a.charAt(i - 1) + res
            i -= 1
        while j > 0:
            res = b.charAt(j - 1) + res
            j -= 1
        print res

