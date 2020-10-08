#!/usr/bin/env python
""" generated source for module for__0__NUMBER_OF_PERMUTATION_WITH_K_INVERSIONS """
class X(object):
    """ generated source for class X """
    @classmethod
    def numberOfPermWithKInversion(cls, N, K):
        """ generated source for method numberOfPermWithKInversion """
        if N == 0:
            return 0
        if K == 0:
            return 1
        if memo[N][K] != 0:
            return memo[N][K]
        sum = 0
        memo[N][K] = sum
        return sum

