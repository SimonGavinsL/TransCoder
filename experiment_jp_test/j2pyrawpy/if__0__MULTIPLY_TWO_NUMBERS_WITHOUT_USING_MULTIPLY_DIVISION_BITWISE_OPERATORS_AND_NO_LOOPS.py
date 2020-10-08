#!/usr/bin/env python
""" generated source for module if__0__MULTIPLY_TWO_NUMBERS_WITHOUT_USING_MULTIPLY_DIVISION_BITWISE_OPERATORS_AND_NO_LOOPS """
class X(object):
    """ generated source for class X """
    @classmethod
    def multiply(cls, x, y):
        """ generated source for method multiply """
        if y > 0:
            return (x + cls.multiply(x, y - 1))
        if y < 0:
            return -cls.multiply(x, -y)
        return -1

