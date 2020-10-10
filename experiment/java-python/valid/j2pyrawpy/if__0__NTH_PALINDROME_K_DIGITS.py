#!/usr/bin/env python
""" generated source for module if__0__NTH_PALINDROME_K_DIGITS """
class X(object):
    """ generated source for class X """
    @classmethod
    def nthPalindrome(cls, n, k):
        """ generated source for method nthPalindrome """
        temp = (k / 2) if (k & 1) != 0 else (k / 2 - 1)
        palindrome = (Math.pow(10, temp))
        palindrome += n - 1
        print palindrome,
        while palindrome > 0:
            print palindrome % 10,
            palindrome /= 10
        print " "

