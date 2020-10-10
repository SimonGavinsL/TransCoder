#!/usr/bin/env python
""" generated source for module if__0__DYNAMIC_PROGRAMMING_SET_4_LONGEST_COMMON_SUBSEQUENCE """
class X(object):
    """ generated source for class X """
    def lcs(self, X, Y, m, n):
        """ generated source for method lcs """
        if X[m - 1] == Y[n - 1]:
            return 1 + self.lcs(X, Y, m - 1, n - 1)
        else:
            return max(self.lcs(X, Y, m, n - 1), self.lcs(X, Y, m - 1, n))

