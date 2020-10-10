#!/usr/bin/env python
""" generated source for module for__0__PROGRAM_DECIMAL_HEXADECIMAL_CONVERSION """
class X(object):
    """ generated source for class X """
    @classmethod
    def decToHexa(cls, n):
        """ generated source for method decToHexa """
        hexaDeciNum = [None]*100
        i = 0
        while n != 0:
            temp = n % 16
            if temp < 10:
                hexaDeciNum[i] = ((temp + 48))
                i += 1
            else:
                hexaDeciNum[i] = ((temp + 55))
                i += 1
            n = n / 16

