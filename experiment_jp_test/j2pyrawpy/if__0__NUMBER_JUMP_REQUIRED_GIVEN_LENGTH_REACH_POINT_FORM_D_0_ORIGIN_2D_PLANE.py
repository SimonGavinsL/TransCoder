#!/usr/bin/env python
""" generated source for module if__0__NUMBER_JUMP_REQUIRED_GIVEN_LENGTH_REACH_POINT_FORM_D_0_ORIGIN_2D_PLANE """
class X(object):
    """ generated source for class X """
    @classmethod
    def minJumps(cls, a, b, d):
        """ generated source for method minJumps """
        temp = a
        a = Math.min(a, b)
        b = Math.max(temp, b)
        if d == 0:
            return 0
        if d == a:
            return 1
        return 2

