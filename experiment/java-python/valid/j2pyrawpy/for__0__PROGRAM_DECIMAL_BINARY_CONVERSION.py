#!/usr/bin/env python
""" generated source for module for__0__PROGRAM_DECIMAL_BINARY_CONVERSION """
class X(object):
    """ generated source for class X """
    @classmethod
    def decToBinary(cls, n):
        """ generated source for method decToBinary """
        binaryNum = [None]*32
        i = 0
        while n > 0:
            binaryNum[i] = n % 2
            n = n / 2
            i += 1

