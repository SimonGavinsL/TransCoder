#!/usr/bin/env python
""" generated source for module if__0__PROGRAM_FOR_NTH_FIBONACCI_NUMBER_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def fib(cls, n):
        """ generated source for method fib """
        if n == 1 or n == 2:
            return (f[n] = 1)
        if f[n] != 0:
            return f[n]
        k = (n + 1) / 2 if (n & 1) == 1 else n / 2
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) if (n & 1) == 1 else (2 * fib(k - 1) + fib(k)) * fib(k)
        return f[n]

