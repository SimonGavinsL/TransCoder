#!/usr/bin/env python
""" generated source for module for__0__SUPER_PRIME """
class X(object):
    """ generated source for class X """
    @classmethod
    def SieveOfEratosthenes(cls, n, isPrime):
        """ generated source for method SieveOfEratosthenes """
        isPrime[0] = isPrime[1] = False
        p = 2
        while p * p <= n:
            if isPrime[p] == True:
                while i <= n:
                    i += p
            p += 1

