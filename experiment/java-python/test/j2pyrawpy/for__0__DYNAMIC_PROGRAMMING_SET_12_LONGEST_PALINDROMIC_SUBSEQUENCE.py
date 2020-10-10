#!/usr/bin/env python
""" generated source for module for__0__DYNAMIC_PROGRAMMING_SET_12_LONGEST_PALINDROMIC_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    @classmethod
    def lps(cls, seq):
        """ generated source for method lps """
        n = len(seq)
        i = int()
        j = int()
        cl = int()
        L = [None]*n
        while cl <= n:
            while i < n - cl + 1:
                j = i + cl - 1
                if seq.charAt(i) == seq.charAt(j) and cl == 2:
                    L[i][j] = 2
                elif seq.charAt(i) == seq.charAt(j):
                    L[i][j] = L[i + 1][j - 1] + 2
                else:
                    L[i][j] = max(L[i][j - 1], L[i + 1][j])
                i += 1
            cl += 1
        return L[0][n - 1]

