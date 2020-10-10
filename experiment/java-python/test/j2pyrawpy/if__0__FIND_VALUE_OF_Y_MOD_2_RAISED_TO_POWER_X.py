#!/usr/bin/env python
""" generated source for module if__0__FIND_VALUE_OF_Y_MOD_2_RAISED_TO_POWER_X """
class X(object):
    """ generated source for class X """
    @classmethod
    def yMod(cls, y, x):
        """ generated source for method yMod """
        if x > 63:
            return y
        return (y % (1 << (x)))

