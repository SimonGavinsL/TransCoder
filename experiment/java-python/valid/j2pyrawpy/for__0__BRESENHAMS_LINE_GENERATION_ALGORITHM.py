#!/usr/bin/env python
""" generated source for module for__0__BRESENHAMS_LINE_GENERATION_ALGORITHM """
class X(object):
    """ generated source for class X """
    @classmethod
    def bresenham(cls, x1, y1, x2, y2):
        """ generated source for method bresenham """
        m_new = 2 * (y2 - y1)
        slope_error_new = m_new - (x2 - x1)

