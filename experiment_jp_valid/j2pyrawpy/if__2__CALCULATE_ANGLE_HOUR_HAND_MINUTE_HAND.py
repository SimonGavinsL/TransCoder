#!/usr/bin/env python
""" generated source for module if__2__CALCULATE_ANGLE_HOUR_HAND_MINUTE_HAND """
class X(object):
    """ generated source for class X """
    @classmethod
    def calcAngle(cls, h, m):
        """ generated source for method calcAngle """
        hour_angle = ((0.5 * (h * 60 + m)))
        minute_angle = ((6 * m))
        angle = Math.abs(hour_angle - minute_angle)
        angle = Math.min(360 - angle, angle)
        return angle

