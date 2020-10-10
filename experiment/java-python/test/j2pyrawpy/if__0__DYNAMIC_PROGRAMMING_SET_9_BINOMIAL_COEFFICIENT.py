#!/usr/bin/env python
""" generated source for module if__0__DYNAMIC_PROGRAMMING_SET_9_BINOMIAL_COEFFICIENT """
class X(object):
    """ generated source for class X """
    @classmethod
    def binomialCoeff(cls, n, k):
        """ generated source for method binomialCoeff """
        return cls.binomialCoeff(n - 1, k - 1) + cls.binomialCoeff(n - 1, k)

