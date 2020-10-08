#!/usr/bin/env python
""" generated source for module if__1__ENTRINGER_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def zigzag(cls, n, k):
        """ generated source for method zigzag """
        return cls.zigzag(n, k - 1) + cls.zigzag(n - 1, n - k)

