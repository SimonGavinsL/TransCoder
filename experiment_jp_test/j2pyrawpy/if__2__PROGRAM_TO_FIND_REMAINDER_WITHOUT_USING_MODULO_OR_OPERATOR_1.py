#!/usr/bin/env python
""" generated source for module if__2__PROGRAM_TO_FIND_REMAINDER_WITHOUT_USING_MODULO_OR_OPERATOR_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def getRemainder(cls, num, divisor):
        """ generated source for method getRemainder """
        i = 1
        product = 0
        while product <= num:
            product = divisor * i
            i += 1
        return num - (product - divisor)

