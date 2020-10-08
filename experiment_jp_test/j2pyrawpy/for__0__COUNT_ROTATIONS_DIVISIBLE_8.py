#!/usr/bin/env python
""" generated source for module for__0__COUNT_ROTATIONS_DIVISIBLE_8 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countRotationsDivBy8(cls, n):
        """ generated source for method countRotationsDivBy8 """
        len = len(n)
        count = 0
        if len == 1:
            if oneDigit % 8 == 0:
                return 1
            return 0
        if len == 2:
            if first % 8 == 0:
                count += 1
            if second % 8 == 0:
                count += 1
            return count
        threeDigit = int()
        threeDigit = (n.charAt(len - 1) - '0') * 100 + (n.charAt(0) - '0') * 10 + (n.charAt(1) - '0')
        if threeDigit % 8 == 0:
            count += 1
        threeDigit = (n.charAt(len - 2) - '0') * 100 + (n.charAt(len - 1) - '0') * 10 + (n.charAt(0) - '0')
        if threeDigit % 8 == 0:
            count += 1
        return count

