#!/usr/bin/env python
""" generated source for module for__0__MAXIMUM_SUM_ABSOLUTE_DIFFERENCE_ARRAY """
class X(object):
    """ generated source for class X """
    @classmethod
    def MaxSumDifference(cls, a, n):
        """ generated source for method MaxSumDifference """
        finalSequence = ArrayList()
        Arrays.sort(a)
        MaximumSum = 0
        i = 0
        while i < n - 1:
            MaximumSum = MaximumSum + Math.abs(finalSequence.get(i) - finalSequence.get(i + 1))
            i += 1
        MaximumSum = MaximumSum + Math.abs(finalSequence.get(n - 1) - finalSequence.get(0))
        return MaximumSum

