#!/usr/bin/env python
""" generated source for module if__0__COUNT_OBTUSE_ANGLES_CIRCLE_K_EQUIDISTANT_POINTS_2_GIVEN_POINTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countObtuseAngles(cls, a, b, k):
        """ generated source for method countObtuseAngles """
        c1 = (b - a) - 1
        c2 = (k - b) + (a - 1)
        return min(c1, c2)

