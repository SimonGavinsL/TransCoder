#!/usr/bin/env python
""" generated source for module for__0__PROGRAM_DECIMAL_OCTAL_CONVERSION """
class X(object):
    """ generated source for class X """
    @classmethod
    def decToOctal(cls, n):
        """ generated source for method decToOctal """
        octalNum = [None]*100
        i = 0
        while n != 0:
            octalNum[i] = n % 8
            n = n / 8
            i += 1

