#!/usr/bin/env python
""" generated source for module if__0__CHECK_WHETHER_LARGE_NUMBER_DIVISIBLE_7 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isDivisible7(cls, num):
        """ generated source for method isDivisible7 """
        n = len(num)
        if n % 3 == 1:
            num = "00" + num
        if n % 3 == 2:
            num = "0" + num
        n = len(num)
        gSum = 0
        p = 1
        return (gSum % 7 == 0)

