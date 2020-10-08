#!/usr/bin/env python
""" generated source for module if__0__CHECK_WHETHER_POINT_EXISTS_CIRCLE_SECTOR_NOT """
class X(object):
    """ generated source for class X """
    @classmethod
    def checkPoint(cls, radius, x, y, percent, startAngle):
        """ generated source for method checkPoint """
        endAngle = 360 / percent + startAngle
        polarradius = Math.sqrt(x * x + y * y)
        Angle = Math.atan(y / x)

