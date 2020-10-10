#!/usr/bin/env python
""" generated source for module if__3__SPLIT_N_MAXIMUM_COMPOSITE_NUMBERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, n):
        """ generated source for method count """
        rem = n % 4
        if rem == 3:
            if n < 15:
                return -1
            return (n - 15) / 4 + 2
        return 0

