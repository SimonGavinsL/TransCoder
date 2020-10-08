#!/usr/bin/env python
""" generated source for module for__0__SMALLEST_ELEMENT_REPEATED_EXACTLY_K_TIMES_NOT_LIMITED_SMALL_RANGE """
class X(object):
    """ generated source for class X """
    @classmethod
    def smallestKFreq(cls, a, n, k):
        """ generated source for method smallestKFreq """
        m = HashMap()
        res = Integer.MAX_VALUE
        s = m.keySet()
        for temp in s:
            if m.get(temp) == k:
                res = Math.min(res, temp)
        return res if (res != Integer.MAX_VALUE) else -1

