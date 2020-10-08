#!/usr/bin/env python
""" generated source for module for__0__HARDY_RAMANUJAN_THEOREM """
class X(object):
    """ generated source for class X """
    @classmethod
    def exactPrimeFactorCount(cls, n):
        """ generated source for method exactPrimeFactorCount """
        count = 0
        if n % 2 == 0:
            count += 1
            while n % 2 == 0:
        if n > 2:
            count += 1
        return count

