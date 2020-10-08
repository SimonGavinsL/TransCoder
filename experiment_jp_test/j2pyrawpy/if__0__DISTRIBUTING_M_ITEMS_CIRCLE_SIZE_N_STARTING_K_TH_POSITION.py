#!/usr/bin/env python
""" generated source for module if__0__DISTRIBUTING_M_ITEMS_CIRCLE_SIZE_N_STARTING_K_TH_POSITION """
class X(object):
    """ generated source for class X """
    @classmethod
    def lastPosition(cls, n, m, k):
        """ generated source for method lastPosition """
        m = m - (n - k + 1)
        return n if (m % n == 0) else (m % n)

