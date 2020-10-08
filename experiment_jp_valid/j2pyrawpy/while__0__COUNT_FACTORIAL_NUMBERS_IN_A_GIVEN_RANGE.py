#!/usr/bin/env python
""" generated source for module while__0__COUNT_FACTORIAL_NUMBERS_IN_A_GIVEN_RANGE """
class X(object):
    """ generated source for class X """
    @classmethod
    def countFact(cls, low, high):
        """ generated source for method countFact """
        fact = 1
        x = 1
        res = 0
        while fact <= high:
            res += 1
            fact = fact * x
            x += 1
        return res

