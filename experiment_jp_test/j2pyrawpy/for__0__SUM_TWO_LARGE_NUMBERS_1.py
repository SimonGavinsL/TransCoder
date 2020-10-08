#!/usr/bin/env python
""" generated source for module for__0__SUM_TWO_LARGE_NUMBERS_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def findSum(cls, str1, str2):
        """ generated source for method findSum """
        if len(str1) > len(str2):
            str1 = str2
            str2 = t
        str_ = " "
        n1 = len(str1)
        n2 = len(str2)
        diff = n2 - n1
        carry = 0
        i = n2 - n1 - 1
        while i >= 0:
            str_ += ((sum % 10 + '0'))
            carry = sum / 10
            i -= 1
        if carry > 0:
            str_ += ((carry + '0'))
        return StringBuilder(str_).reverse().__str__()

