#!/usr/bin/env python
""" generated source for module for__1__MAXIMUM_SUM_ABSOLUTE_DIFFERENCE_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def MaxSumDifference(cls, a, n):
        """ generated source for method MaxSumDifference """
        finalSequence = ArrayList()
        Arrays.sort(a)
        MaximumSum = 0
        MaximumSum = MaximumSum + Math.abs(finalSequence.get(n - 1) - finalSequence.get(0))
        return MaximumSum

