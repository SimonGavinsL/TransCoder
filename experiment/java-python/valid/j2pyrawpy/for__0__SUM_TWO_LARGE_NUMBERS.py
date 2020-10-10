#!/usr/bin/env python
""" generated source for module for__0__SUM_TWO_LARGE_NUMBERS """
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
        str1 = StringBuilder(str1).reverse().__str__()
        str2 = StringBuilder(str2).reverse().__str__()
        carry = 0
        i = n1
        while i < n2:
            str_ += ((sum % 10 + '0'))
            carry = sum / 10
            i += 1
        if carry > 0:
            str_ += ((carry + '0'))
        str_ = StringBuilder(str_).reverse().__str__()
        return str_

