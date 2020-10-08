#!/usr/bin/env python
""" generated source for module for__2__DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isSubsetSum(cls, set, n, sum):
        """ generated source for method isSubsetSum """
        subset = [None]*sum + 1
        return subset[sum][n]

