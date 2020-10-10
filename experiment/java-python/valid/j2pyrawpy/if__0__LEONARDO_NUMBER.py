#!/usr/bin/env python
""" generated source for module if__0__LEONARDO_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def leonardo(cls, n):
        """ generated source for method leonardo """
        return (cls.leonardo(n - 1) + cls.leonardo(n - 2) + 1)

