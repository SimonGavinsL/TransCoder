#!/usr/bin/env python
""" generated source for module if__0__COUNT_ROTATIONS_DIVISIBLE_4 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countRotations(cls, n):
        """ generated source for method countRotations """
        len = len(n)
        twoDigit = int()
        count = 0
        twoDigit = (n.charAt(len - 1) - '0') * 10 + (n.charAt(0) - '0')
        if twoDigit % 4 == 0:
            count += 1
        return count

