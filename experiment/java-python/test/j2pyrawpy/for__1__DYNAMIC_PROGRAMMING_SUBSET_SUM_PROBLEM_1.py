#!/usr/bin/env python
""" generated source for module for__1__DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isSubsetSum(cls, set, n, sum):
        """ generated source for method isSubsetSum """
        subset = [None]*sum + 1
        i = 1
        while i <= sum:
            while j <= n:
                subset[i][j] = subset[i][j - 1]
                if i >= set[j - 1]:
                    subset[i][j] = subset[i][j] or subset[i - set[j - 1]][j - 1]
                j += 1
            i += 1
        return subset[sum][n]

