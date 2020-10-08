#!/usr/bin/env python
""" generated source for module while__0__PROGRAM_CHECK_PLUS_PERFECT_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def checkplusperfect(cls, x):
        """ generated source for method checkplusperfect """
        temp = x
        n = 0
        x = temp
        sum = 0
        while x != 0:
            sum += Math.pow(x % 10, n)
            x /= 10
        return (sum == temp)

