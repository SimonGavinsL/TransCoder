#!/usr/bin/env python
""" generated source for module for__0__POLICEMEN_CATCH_THIEVES """
class X(object):
    """ generated source for class X """
    @classmethod
    def policeThief(cls, arr, n, k):
        """ generated source for method policeThief """
        res = 0
        thi = ArrayList()
        pol = ArrayList()
        l = 0
        r = 0
        while l < len(thi) and r < len(pol):
            if Math.abs(thi.get(l) - pol.get(r)) <= k:
                res += 1
                l += 1
                r += 1
            elif thi.get(l) < pol.get(r):
                l += 1
            else:
                r += 1
        return res

