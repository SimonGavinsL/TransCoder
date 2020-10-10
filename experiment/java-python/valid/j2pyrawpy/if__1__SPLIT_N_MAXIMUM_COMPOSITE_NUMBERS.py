#!/usr/bin/env python
""" generated source for module if__1__SPLIT_N_MAXIMUM_COMPOSITE_NUMBERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, n):
        """ generated source for method count """
        rem = n % 4
        if rem == 1:
            if n < 9:
                return -1
            return (n - 9) / 4 + 1
        if rem == 2:
            return (n - 6) / 4 + 1
        if rem == 3:
            if n < 15:
                return -1
            return (n - 15) / 4 + 2
        return 0

