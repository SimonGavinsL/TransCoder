#!/usr/bin/env python
""" generated source for module if__0__DYNAMIC_PROGRAMMING_SUBSET_SUM_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def isSubsetSum(cls, set, n, sum):
        """ generated source for method isSubsetSum """
        if n == 0 and sum != 0:
            return False
        if set[n - 1] > sum:
            return cls.isSubsetSum(set, n - 1, sum)
        return cls.isSubsetSum(set, n - 1, sum) or cls.isSubsetSum(set, n - 1, sum - set[n - 1])

