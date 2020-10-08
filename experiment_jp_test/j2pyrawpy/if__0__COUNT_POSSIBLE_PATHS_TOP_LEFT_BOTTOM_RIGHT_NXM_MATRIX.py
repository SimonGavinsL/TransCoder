#!/usr/bin/env python
""" generated source for module if__0__COUNT_POSSIBLE_PATHS_TOP_LEFT_BOTTOM_RIGHT_NXM_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def numberOfPaths(cls, m, n):
        """ generated source for method numberOfPaths """
        return cls.numberOfPaths(m - 1, n) + cls.numberOfPaths(m, n - 1)

