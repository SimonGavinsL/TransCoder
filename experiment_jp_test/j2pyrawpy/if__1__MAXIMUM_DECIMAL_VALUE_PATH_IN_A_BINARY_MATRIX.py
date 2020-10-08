#!/usr/bin/env python
""" generated source for module if__1__MAXIMUM_DECIMAL_VALUE_PATH_IN_A_BINARY_MATRIX """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxDecimalValue(cls, mat, i, j, p):
        """ generated source for method maxDecimalValue """
        result = Math.max(cls.maxDecimalValue(mat, i, j + 1, p + 1), cls.maxDecimalValue(mat, i + 1, j, p + 1))

