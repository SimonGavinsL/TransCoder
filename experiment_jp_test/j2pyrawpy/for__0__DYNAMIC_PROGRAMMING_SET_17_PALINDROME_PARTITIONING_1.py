#!/usr/bin/env python
""" generated source for module for__0__DYNAMIC_PROGRAMMING_SET_17_PALINDROME_PARTITIONING_1 """
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
                i += 1
            L += 1
        while i < n:
            if P[0][i] == True:
                C[i] = 0
            else:
                C[i] = Integer.MAX_VALUE
                while j < i:
                    if P[j + 1][i] == True and 1 + C[j] < C[i]:
                        C[i] = 1 + C[j]
                    j += 1
            i += 1
        return C[n - 1]

