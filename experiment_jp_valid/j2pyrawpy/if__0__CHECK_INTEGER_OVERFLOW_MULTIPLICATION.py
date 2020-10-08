#!/usr/bin/env python
""" generated source for module if__0__CHECK_INTEGER_OVERFLOW_MULTIPLICATION """
class X(object):
    """ generated source for class X """
    @classmethod
    def isOverflow(cls, a, b):
        """ generated source for method isOverflow """
        result = a * b
        if a == result / b:
            return False
        else:
            return True

