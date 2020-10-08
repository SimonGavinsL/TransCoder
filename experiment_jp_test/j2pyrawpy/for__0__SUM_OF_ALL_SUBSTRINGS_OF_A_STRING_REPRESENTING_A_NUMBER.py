#!/usr/bin/env python
""" generated source for module for__0__SUM_OF_ALL_SUBSTRINGS_OF_A_STRING_REPRESENTING_A_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def sumOfSubstrings(cls, num):
        """ generated source for method sumOfSubstrings """
        n = len(num)
        sumofdigit = [None]*n
        sumofdigit[0] = num.charAt(0) - '0'
        res = sumofdigit[0]
        return res

