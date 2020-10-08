#!/usr/bin/env python
""" generated source for module if__0__DECIMAL_BINARY_CONVERSION_WITHOUT_USING_ARITHMETIC_OPERATORS """
class X(object):
    """ generated source for class X """
    @classmethod
    def decToBin(cls, n):
        """ generated source for method decToBin """
        bin = " "
        while n > 0:
            bin = ('0' if (n & 1) == 0 else '1') + bin
            n >>= 1
        return bin

