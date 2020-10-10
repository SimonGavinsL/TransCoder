#!/usr/bin/env python
""" generated source for module if__0__PROGRAM_FIND_STRING_START_END_GEEKS """
class X(object):
    """ generated source for class X """
    @classmethod
    def isCornerPresent(cls, str_, corner):
        """ generated source for method isCornerPresent """
        n = len(str_)
        cl = len(corner)
        return (str_.substring(0, cl) == corner and str_.substring(n - cl, n) == corner)

