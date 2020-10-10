#!/usr/bin/env python
""" generated source for module if__1__EULERIAN_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def eulerian(cls, n, m):
        """ generated source for method eulerian """
        return (n - m) * cls.eulerian(n - 1, m - 1) + (m + 1) * cls.eulerian(n - 1, m)

