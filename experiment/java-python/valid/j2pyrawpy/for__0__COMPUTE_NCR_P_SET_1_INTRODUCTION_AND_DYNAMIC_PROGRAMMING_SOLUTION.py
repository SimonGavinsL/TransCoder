#!/usr/bin/env python
""" generated source for module for__0__COMPUTE_NCR_P_SET_1_INTRODUCTION_AND_DYNAMIC_PROGRAMMING_SOLUTION """
class X(object):
    """ generated source for class X """
    @classmethod
    def nCrModp(cls, n, r, p):
        """ generated source for method nCrModp """
        C = [None]*r + 1
        Arrays.fill(C, 0)
        C[0] = 1
        return C[r]

