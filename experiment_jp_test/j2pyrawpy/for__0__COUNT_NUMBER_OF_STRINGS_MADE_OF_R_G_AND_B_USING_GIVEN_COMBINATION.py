#!/usr/bin/env python
""" generated source for module for__0__COUNT_NUMBER_OF_STRINGS_MADE_OF_R_G_AND_B_USING_GIVEN_COMBINATION """
class X(object):
    """ generated source for class X """
    @classmethod
    def possibleStrings(cls, n, r, b, g):
        """ generated source for method possibleStrings """
        fact = [None]*n + 1
        fact[0] = 1
        left = n - (r + g + b)
        sum = 0
        i = 0
        while i <= left:
            while j <= left - i:
                sum = sum + fact[n] / (fact[i + r] * fact[j + b] * fact[k + g])
                j += 1
            i += 1
        return sum

