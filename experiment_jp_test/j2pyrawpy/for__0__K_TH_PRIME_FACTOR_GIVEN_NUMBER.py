#!/usr/bin/env python
""" generated source for module for__0__K_TH_PRIME_FACTOR_GIVEN_NUMBER """
class X(object):
    """ generated source for class X """
    @classmethod
    def kPrimeFactor(cls, n, k):
        """ generated source for method kPrimeFactor """
        while n % 2 == 0:
            k -= 1
            n = n / 2
            if k == 0:
                return 2
        if n > 2 and k == 1:
            return n
        return -1

