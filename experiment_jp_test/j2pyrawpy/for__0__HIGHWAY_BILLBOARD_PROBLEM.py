#!/usr/bin/env python
""" generated source for module for__0__HIGHWAY_BILLBOARD_PROBLEM """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxRevenue(cls, m, x, revenue, n, t):
        """ generated source for method maxRevenue """
        maxRev = [None]*m + 1
        nxtbb = 0
        i = 1
        while i <= m:
            if nxtbb < n:
                if x[nxtbb] != i:
                    maxRev[i] = maxRev[i - 1]
                else:
                    if i <= t:
                        maxRev[i] = Math.max(maxRev[i - 1], revenue[nxtbb])
                    else:
                        maxRev[i] = Math.max(maxRev[i - t - 1] + revenue[nxtbb], maxRev[i - 1])
                    nxtbb += 1
            else:
                maxRev[i] = maxRev[i - 1]
            i += 1
        return maxRev[m]

