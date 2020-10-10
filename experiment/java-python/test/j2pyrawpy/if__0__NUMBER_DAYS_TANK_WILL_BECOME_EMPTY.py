#!/usr/bin/env python
""" generated source for module if__0__NUMBER_DAYS_TANK_WILL_BECOME_EMPTY """
class X(object):
    """ generated source for class X """
    @classmethod
    def minDaysToEmpty(cls, C, l):
        """ generated source for method minDaysToEmpty """
        eq_root = (Math.sqrt(1 + 8 * (C - l)) - 1) / 2
        return ((Math.ceil(eq_root) + l))

