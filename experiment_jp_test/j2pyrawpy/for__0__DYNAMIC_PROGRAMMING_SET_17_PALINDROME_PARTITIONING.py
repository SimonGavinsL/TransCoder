#!/usr/bin/env python
""" generated source for module for__0__DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING """
class X(object):
    """ generated source for class X """
    @classmethod
    def minPalPartion(cls, str_):
        """ generated source for method minPalPartion """
        n = len(str_)
        C = [None]*n
        P = [None]*n
        i = int()
        j = int()
        k = int()
        L = int()
        while L <= n:
            while i < n - L + 1:
                j = i + L - 1
                if L == 2:
                    P[i][j] = (str_.charAt(i) == str_.charAt(j))
                else:
                    P[i][j] = (str_.charAt(i) == str_.charAt(j)) and P[i + 1][j - 1]
                if P[i][j] == True:
                    C[i][j] = 0
                else:
                    C[i][j] = Integer.MAX_VALUE
                    while k <= j - 1:
                        k += 1
                i += 1
            L += 1
        return C[0][n - 1]

