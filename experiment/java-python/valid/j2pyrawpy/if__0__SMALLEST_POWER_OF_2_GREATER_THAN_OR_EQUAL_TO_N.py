#!/usr/bin/env python
""" generated source for module if__0__SMALLEST_POWER_OF_2_GREATER_THAN_OR_EQUAL_TO_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def nextPowerOf2(cls, n):
        """ generated source for method nextPowerOf2 """
        count = 0
        while n != 0:
            n >>= 1
            count += 1
        return 1 << count

