#!/usr/bin/env python
""" generated source for module for__0__DECIMAL_REPRESENTATION_GIVEN_BINARY_STRING_DIVISIBLE_10_NOT """
class X(object):
    """ generated source for class X """
    @classmethod
    def isDivisibleBy10(cls, bin):
        """ generated source for method isDivisibleBy10 """
        n = len(bin)
        if bin.charAt(n - 1) == '1':
            return False
        sum = 0
        if sum % 10 == 0:
            return True
        return False

