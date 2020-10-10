#!/usr/bin/env python
""" generated source for module if__0__DELANNOY_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def dealnnoy(cls, n, m):
        """ generated source for method dealnnoy """
        return cls.dealnnoy(m - 1, n) + cls.dealnnoy(m - 1, n - 1) + cls.dealnnoy(m, n - 1)

