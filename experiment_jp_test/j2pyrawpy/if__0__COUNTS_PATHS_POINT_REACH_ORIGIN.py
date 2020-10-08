#!/usr/bin/env python
""" generated source for module if__0__COUNTS_PATHS_POINT_REACH_ORIGIN """
class X(object):
    """ generated source for class X """
    @classmethod
    def countPaths(cls, n, m):
        """ generated source for method countPaths """
        return (cls.countPaths(n - 1, m) + cls.countPaths(n, m - 1))

