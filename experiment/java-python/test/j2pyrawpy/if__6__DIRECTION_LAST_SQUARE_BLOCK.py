#!/usr/bin/env python
""" generated source for module if__6__DIRECTION_LAST_SQUARE_BLOCK """
class X(object):
    """ generated source for class X """
    @classmethod
    def direction(cls, R, C):
        """ generated source for method direction """
        if R != C and R % 2 == 0 and C % 2 == 0 and R > C:
            print " Up "
            return
        if R != C and R % 2 == 0 and C % 2 != 0 and R > C:
            print " Down "
            return
        if R != C and R % 2 != 0 and C % 2 == 0 and R < C:
            print " Right "
            return

