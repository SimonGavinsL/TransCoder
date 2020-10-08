#!/usr/bin/env python
""" generated source for module for__0__CHECK_DIVISIBILITY_LARGE_NUMBER_999 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isDivisible999(cls, num):
        """ generated source for method isDivisible999 """
        n = len(num)
        if n == 0 and num.charAt(0) == '0':
            return True
        if n % 3 == 1:
            num = "00" + num
        if n % 3 == 2:
            num = "0" + num
        gSum = 0
        if gSum > 1000:
            num = Integer.toString(gSum)
            n = len(num)
            gSum = 1 if isDivisible999(num) else 0
        return (gSum == 999)

