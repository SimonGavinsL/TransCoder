#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_SUM_INCREASING_SUBSEQUENCE_FROM_A_PREFIX_AND_A_GIVEN_ELEMENT_AFTER_PREFIX_IS_MUST """
class X(object):
    """ generated source for class X """
    @classmethod
    def pre_compute(cls, a, n, index, k):
        """ generated source for method pre_compute """
        dp = [None]*n
        i = 1
        while i < n:
            while j < n:
                if a[j] > a[i] and j > i:
                    if dp[i - 1][i] + a[j] > dp[i - 1][j]:
                        dp[i][j] = dp[i - 1][i] + a[j]
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                j += 1
            i += 1
        return dp[index][k]

