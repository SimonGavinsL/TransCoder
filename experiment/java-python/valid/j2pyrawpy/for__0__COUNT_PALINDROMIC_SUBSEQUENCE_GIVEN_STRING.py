#!/usr/bin/env python
""" generated source for module for__0__COUNT_PALINDROMIC_SUBSEQUENCE_GIVEN_STRING """
class X(object):
    """ generated source for class X """
    @classmethod
    def countPS(cls, str_):
        """ generated source for method countPS """
        N = len(str_)
        cps = [None]*N + 1
        L = 2
        while L <= N:
            while i < N:
                if k < N:
                    if str_.charAt(i) == str_.charAt(k):
                        cps[i][k] = cps[i][k - 1] + cps[i + 1][k] + 1
                    else:
                        cps[i][k] = cps[i][k - 1] + cps[i + 1][k] - cps[i + 1][k - 1]
                i += 1
            L += 1
        return cps[0][N - 1]

