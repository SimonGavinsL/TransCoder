#!/usr/bin/env python
""" generated source for module if__2__COUNT_STRINGS_CAN_FORMED_USING_B_C_GIVEN_CONSTRAINTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countStr(cls, n, bCount, cCount):
        """ generated source for method countStr """
        res = cls.countStr(n - 1, bCount, cCount)
        res += countStr(n - 1, bCount - 1, cCount)
        res += countStr(n - 1, bCount, cCount - 1)
        return res

