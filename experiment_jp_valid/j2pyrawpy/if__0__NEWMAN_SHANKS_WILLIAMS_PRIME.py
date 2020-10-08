#!/usr/bin/env python
""" generated source for module if__0__NEWMAN_SHANKS_WILLIAMS_PRIME """
class X(object):
    """ generated source for class X """
    @classmethod
    def nswp(cls, n):
        """ generated source for method nswp """
        return 2 * cls.nswp(n - 1) + cls.nswp(n - 2)

