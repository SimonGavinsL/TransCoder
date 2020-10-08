#!/usr/bin/env python
""" generated source for module if__0__CHECK_TWO_GIVEN_CIRCLES_TOUCH_INTERSECT """
class X(object):
    """ generated source for class X """
    @classmethod
    def circle(cls, x1, y1, x2, y2, r1, r2):
        """ generated source for method circle """
        distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        radSumSq = (r1 + r2) * (r1 + r2)

