#!/usr/bin/env python
""" generated source for module for__0__SUM_LARGEST_PRIME_FACTOR_NUMBER_LESS_EQUAL_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def sumOfLargePrimeFactor(cls, n):
        """ generated source for method sumOfLargePrimeFactor """
        prime = [None]*n + 1
        sum = 0
        Arrays.fill(prime, 0)
        max = n / 2
        p = 2
        while p <= n:
            if prime[p] != 0:
                sum += prime[p]
            else:
                sum += p
            p += 1
        return sum

