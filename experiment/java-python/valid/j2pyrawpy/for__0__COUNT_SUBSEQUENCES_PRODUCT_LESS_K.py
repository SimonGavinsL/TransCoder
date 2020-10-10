#!/usr/bin/env python
""" generated source for module for__0__COUNT_SUBSEQUENCES_PRODUCT_LESS_K """
class X(object):
    """ generated source for class X """
    @classmethod
    def productSubSeqCount(cls, arr, k):
        """ generated source for method productSubSeqCount """
        n = len(arr)
        dp = [None]*k + 1
        return dp[k][n]

