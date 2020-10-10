#!/usr/bin/env python
""" generated source for module while__0__MINIMIZE_MAXAI_BJ_CK_MINAI_BJ_CK_THREE_DIFFERENT_SORTED_ARRAYS """
class X(object):
    """ generated source for class X """
    @classmethod
    def solve(cls, A, B, C):
        """ generated source for method solve """
        i = int()
        j = int()
        k = int()
        i = A.length - 1
        j = B.length - 1
        k = C.length - 1
        min_diff = int()
        current_diff = int()
        max_term = int()
        min_diff = Math.abs(Math.max(A[i], Math.max(B[j], C[k])) - Math.min(A[i], Math.min(B[j], C[k])))
        return min_diff

