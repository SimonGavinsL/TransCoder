#!/usr/bin/env python
""" generated source for module if__0__COMPOSITE_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def isComposite(cls, n):
        """ generated source for method isComposite """
        if n <= 3:
            print " False "
        if n % 2 == 0 or n % 3 == 0:
            return True
        return False

