#!/usr/bin/env python
""" generated source for module if__0__PROGRAM_CHECK_WATER_TANK_OVERFLOWS_N_SOLID_BALLS_DIPPED_WATER_TANK """
class X(object):
    """ generated source for class X """
    @classmethod
    def overflow(cls, H, r, h, N, R):
        """ generated source for method overflow """
        tank_cap = 3.14 * r * r * H
        water_vol = 3.14 * r * r * h
        balls_vol = N * (4 / 3) * 3.14 * R * R * R
        vol = water_vol + balls_vol

