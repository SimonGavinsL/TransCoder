#!/usr/bin/env python
""" generated source for module for__0__NUMBER_WHICH_HAS_THE_MAXIMUM_NUMBER_OF_DISTINCT_PRIME_FACTORS_IN_RANGE_M_TO_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def maximumNumberDistinctPrimeRange(cls, m, n):
        """ generated source for method maximumNumberDistinctPrimeRange """
        factorCount = [None]*n + 1
        prime = [None]*n + 1
        i = 2
        while i <= n:
            if prime[i] == True:
                factorCount[i] = 1
                while j <= n:
                    factorCount[j] += 1
                    prime[j] = False
                    j += i
            i += 1
        max = (factorCount[m])
        num = m
        i = m
        while i <= n:
            if factorCount[i] > max:
                max = (factorCount[i])
                num = i
            i += 1
        return num

