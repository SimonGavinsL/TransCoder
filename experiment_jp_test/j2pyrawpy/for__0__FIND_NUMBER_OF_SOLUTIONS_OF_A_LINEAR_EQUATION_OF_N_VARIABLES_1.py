#!/usr/bin/env python
""" generated source for module for__0__FIND_NUMBER_OF_SOLUTIONS_OF_A_LINEAR_EQUATION_OF_N_VARIABLES_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countSol(cls, coeff, n, rhs):
        """ generated source for method countSol """
        dp = [None]*rhs + 1
        Arrays.fill(dp, 0)
        dp[0] = 1
        return dp[rhs]

