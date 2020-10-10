#!/usr/bin/env python
""" generated source for module for__0__SUM_FIBONACCI_NUMBERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def calculateSum(cls, n):
        """ generated source for method calculateSum """
        if n <= 0:
            return 0
        fibo = [None]*n + 1
        fibo[0] = 0
        fibo[1] = 1
        sum = fibo[0] + fibo[1]
        return sum

